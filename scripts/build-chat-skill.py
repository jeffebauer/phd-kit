#!/usr/bin/env python3
"""Build the single-upload Claude app skill from the plugin's skills.

Copies each plugin skill body (frontmatter removed) into
chat-skill/references/<name>.md, adds the literature-note template,
then zips chat-skill/ as dist/phd-research-kit.zip with the folder
name matching the skill name, as the Claude app requires.

Run from the repo root:  python3 scripts/build-chat-skill.py
"""
import pathlib
import re
import shutil
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "phd" / "skills"
TEMPLATE = ROOT / "plugins" / "phd" / "vault-template" / "_templates" / "literature-note.md"
CHAT = ROOT / "chat-skill"
REFS = CHAT / "references"
DIST = ROOT / "dist"
SKIP = {"setup", "audit", "migrate"}  # Claude Code only; chat-setup.md and audit-and-migrate.md replace them

KEEP = {"chat-setup.md", "audit-and-migrate.md"}  # hand-written chat-only references
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


def main() -> None:
    REFS.mkdir(parents=True, exist_ok=True)
    for old in REFS.glob("*.md"):
        if old.name not in KEEP:
            old.unlink()
    for skill in sorted(SKILLS.iterdir()):
        if not skill.is_dir() or skill.name in SKIP:
            continue
        body = FRONTMATTER.sub("", (skill / "SKILL.md").read_text(encoding="utf-8"), count=1)
        (REFS / f"{skill.name}.md").write_text(body.lstrip(), encoding="utf-8")
    shutil.copyfile(TEMPLATE, REFS / "literature-note-template.md")

    DIST.mkdir(exist_ok=True)
    out = DIST / "phd-research-kit.zip"
    out.unlink(missing_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(CHAT.rglob("*")):
            if f.is_file():
                z.write(f, pathlib.Path("phd-research-kit") / f.relative_to(CHAT))
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
