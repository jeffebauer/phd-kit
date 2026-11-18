#!/usr/bin/env python3
"""Read a Claude data export without loading it all into a conversation.

The export from Settings > Privacy > Export data is one or more zips holding
conversations.json, projects.json and, in some exports, memories.json.
This script only reads; it never changes or uploads anything.

Usage (paths may be zips or unzipped folders; pass every batch zip):
  claude_export.py index   EXPORT... [--out FILE]     list conversations and projects
  claude_export.py show    EXPORT... --id UUID [--max-chars N]   one conversation as Markdown
  claude_export.py project EXPORT... --id UUID --dest DIR        a project's instructions and files
  claude_export.py memory  EXPORT...                              stored memory text, if present

Standard library only. Run with:  uv run claude_export.py ...  (or python3)
"""
import argparse
import json
import pathlib
import re
import sys
import zipfile

NAMES = ("conversations.json", "projects.json", "memories.json")


def load(paths):
    """Merge the JSON files found in every given zip or folder."""
    data = {n: [] for n in NAMES}
    for raw in paths:
        p = pathlib.Path(raw).expanduser()
        if not p.exists():
            sys.exit(f"Not found: {p}")
        if p.is_file() and p.suffix.lower() == ".zip":
            with zipfile.ZipFile(p) as z:
                for member in z.namelist():
                    base = member.rsplit("/", 1)[-1]
                    if base in NAMES:
                        _add(data, base, json.loads(z.read(member).decode("utf-8")))
        elif p.is_dir():
            for base in NAMES:
                for f in p.rglob(base):
                    _add(data, base, json.loads(f.read_text(encoding="utf-8")))
        elif p.name in NAMES:
            _add(data, p.name, json.loads(p.read_text(encoding="utf-8")))
        else:
            sys.exit(f"Not a zip, folder, or export JSON file: {p}")
    if not data["conversations.json"] and not data["projects.json"]:
        sys.exit("No conversations.json or projects.json found. Pass every zip from the export email.")
    return data


def _add(data, name, value):
    if isinstance(value, list):
        data[name].extend(value)
    else:
        data[name].append(value)


def text_of(msg):
    """Message text across export format versions."""
    parts = []
    if isinstance(msg.get("text"), str) and msg["text"].strip():
        parts.append(msg["text"])
    for block in msg.get("content") or []:
        if isinstance(block, dict) and block.get("type") == "text" and block.get("text"):
            if block["text"] not in parts:
                parts.append(block["text"])
    names = [a.get("file_name") for a in (msg.get("attachments") or []) + (msg.get("files") or []) if isinstance(a, dict) and a.get("file_name")]
    if names:
        parts.append("[attached: " + ", ".join(names) + "]")
    return "\n\n".join(parts).strip()


def one_line(s, n):
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def cell(s):
    return (s or "").replace("|", "/")


def cmd_index(data, out):
    projects = {p.get("uuid"): p.get("name") or "(unnamed)" for p in data["projects.json"]}
    convs = sorted(data["conversations.json"], key=lambda c: c.get("updated_at") or c.get("created_at") or "", reverse=True)
    lines = ["# Claude export index", ""]
    lines.append(f"{len(convs)} conversations, {len(data['projects.json'])} projects"
                 + (", memory present" if data["memories.json"] else "") + ".")
    lines += ["", "## Projects", "", "| Name | Files | Has instructions | ID |", "| :- | -: | :- | :- |"]
    for p in data["projects.json"]:
        lines.append(f"| {cell(p.get('name'))} | {len(p.get('docs') or [])} | "
                     f"{'yes' if (p.get('prompt_template') or '').strip() else 'no'} | `{p.get('uuid')}` |")
    lines += ["", "## Conversations (newest first)", "",
              "| Date | Title | Msgs | Project | First message | ID |", "| :- | :- | -: | :- | :- | :- |"]
    for c in convs:
        msgs = c.get("chat_messages") or []
        first = next((text_of(m) for m in msgs if m.get("sender") == "human"), "")
        date = (c.get("updated_at") or c.get("created_at") or "")[:10]
        proj = projects.get(c.get("project_uuid") or (c.get("project") or {}).get("uuid"), "")
        lines.append(f"| {date} | {cell(one_line(c.get('name') or '(untitled)', 70))} | {len(msgs)} | "
                     f"{cell(proj)} | {cell(one_line(first, 90))} | `{c.get('uuid')}` |")
    text = "\n".join(lines) + "\n"
    if out:
        pathlib.Path(out).write_text(text, encoding="utf-8")
        print(f"Wrote {out}: {len(convs)} conversations, {len(data['projects.json'])} projects")
    else:
        sys.stdout.write(text)


def find(items, uuid, what):
    for item in items:
        if item.get("uuid") == uuid:
            return item
    sys.exit(f"No {what} with id {uuid}")


def cmd_show(data, uuid, max_chars):
    c = find(data["conversations.json"], uuid, "conversation")
    out = [f"# {c.get('name') or '(untitled)'}", f"{(c.get('created_at') or '')[:10]} · id `{uuid}`", ""]
    for m in c.get("chat_messages") or []:
        who = "Me" if m.get("sender") == "human" else "Claude"
        out += [f"## {who}", text_of(m), ""]
    text = "\n".join(out)
    if max_chars and len(text) > max_chars:
        text = text[:max_chars] + f"\n\n[truncated at {max_chars} characters of {len(text)}; rerun with a larger --max-chars to see more]"
    sys.stdout.write(text + "\n")


def safe_name(s):
    s = re.sub(r"[^\w.\- ]+", "", s or "file").strip()
    return s[:80] or "file"


def cmd_project(data, uuid, dest):
    p = find(data["projects.json"], uuid, "project")
    d = pathlib.Path(dest).expanduser()
    d.mkdir(parents=True, exist_ok=True)
    written = []
    instr = (p.get("prompt_template") or "").strip()
    if instr:
        (d / "project-instructions.md").write_text(f"# {p.get('name')}: instructions\n\n{instr}\n", encoding="utf-8")
        written.append("project-instructions.md")
    for doc in p.get("docs") or []:
        name = safe_name(doc.get("filename") or doc.get("uuid"))
        if not name.lower().endswith((".md", ".txt")):
            name += ".md"
        target = d / name
        if target.exists():
            target = d / f"{target.stem}-{(doc.get('uuid') or 'x')[:8]}{target.suffix}"
        target.write_text(doc.get("content") or "", encoding="utf-8")
        written.append(target.name)
    print(f"Wrote {len(written)} files to {d}:")
    for w in written:
        print(f"  {w}")


def cmd_memory(data):
    if not data["memories.json"]:
        print("No memories.json in this export. Ask Claude in the app: \"What do you remember about my research?\"")
        return
    for m in data["memories.json"]:
        if isinstance(m, dict):
            if m.get("conversations_memory"):
                print("## Account memory\n\n" + m["conversations_memory"].strip() + "\n")
            for pid, txt in (m.get("project_memories") or {}).items():
                print(f"## Project memory `{pid}`\n\n{str(txt).strip()}\n")
        else:
            print(str(m))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["index", "show", "project", "memory"])
    ap.add_argument("export", nargs="+", help="export zip(s), unzipped folder, or JSON files")
    ap.add_argument("--id")
    ap.add_argument("--out")
    ap.add_argument("--dest")
    ap.add_argument("--max-chars", type=int, default=40000)
    a = ap.parse_args()
    data = load(a.export)
    if a.command == "index":
        cmd_index(data, a.out)
    elif a.command == "show":
        cmd_show(data, a.id or sys.exit("--id is required"), a.max_chars)
    elif a.command == "project":
        if not (a.id and a.dest):
            sys.exit("--id and --dest are required")
        cmd_project(data, a.id, a.dest)
    else:
        cmd_memory(data)


if __name__ == "__main__":
    main()
