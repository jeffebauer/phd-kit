---
name: migrate
description: Bring existing research material into the vault, step by step from the audit plan. Covers Claude chats, Projects and memory (via the Claude data export), papers into Zotero, notes from other apps, and Word or Google Docs files. Use when they say "migrate", "import my old chats", "bring my notes in", or want to act on admin/setup-audit.md.
effort: medium
---

# Migrate into the vault

Work from `admin/setup-audit.md`. If it doesn't exist, run `/phd:audit` first. Do one source per session where possible, tick it off in the audit file when done, and run `/phd:session-checkpoint` between sources.

## Rules for everything imported
- **Ask before writing.** Show what you plan to create, then write it.
- **Mark imported material.** Every file you create gets `source: imported from <where>` and `status: needs-review` in its frontmatter. They clear the status when they've checked it.
- **Citations from old chats are unverified.** Past Claude chats can contain wrong or invented references. Never put a paper into `literature/` or `_index/papers.md` because a chat mentioned it. List it in `inbox/imported-papers.md` with `[UNVERIFIED]`, and only promote it after it's found in Zotero.
- **Research content only.** Skip personal, unrelated, or sensitive material, and anything the audit marked "leave in place". If unsure, ask.
- **Their words stay theirs.** Summarise Claude's past answers briefly; keep their own writing as it is.
- **Nothing leaves the computer.** The export and files are processed locally.

## A. Research profile (always first)
Fill `admin/research-profile.md` (programme, supervisors and what each cares about, milestones, methods and data, key terms, where things live) and the `{{...}}` placeholders in `CLAUDE.md` from the audit answers, the Project instructions, and memory (section B). Ask with the question tool for anything missing, 4 questions at a time. Keep `CLAUDE.md` short: it loads every session; detail belongs in the profile.

## B. Claude chats, Projects, and memory
1. Tell them how to export: on claude.ai or the desktop app (not the phone app), Settings → Privacy → Export data. The email link expires after 24 hours, and a large export arrives as several zips: download all of them. Save them **outside** the vault, for example `Documents/claude-export/`.
2. Ask for the path, then build an index without opening the conversations:
   `uv run "${CLAUDE_SKILL_DIR}/scripts/claude_export.py" index <every zip> --out inbox/claude-export-index.md`
   (Use `python3` instead of `uv run` if uv isn't installed.)
3. Read the index. Group research-looking conversations into 3 to 6 themes by title and first message. Ask with a multi-select question which themes to import. Don't open unrelated chats.
4. **Projects:** for each PhD Project, run `project <zips> --id <uuid> --dest inbox/imported/<project-name>/`. Merge useful instructions into `CLAUDE.md` or the profile; move notes into `synthesis/` or `admin/`; papers mentioned go to `inbox/imported-papers.md`.
5. **Memory:** run `memory <zips>`. Research facts go into the profile. If the export has none, suggest they ask Claude in the app "What do you remember about my research?" and paste the answer.
6. **Chats:** for each chosen conversation, run `show <zips> --id <uuid> --max-chars 40000` and extract only:
   - decisions and arguments they reached → `synthesis/imported-<theme>.md`, one section per conversation with its date
   - papers mentioned → `inbox/imported-papers.md` with `[UNVERIFIED]`
   - open questions → the profile's open questions, or `_sessions/` for today
   Do 5 to 10 conversations, then checkpoint. Long chats are expensive: read the first 40,000 characters and ask before reading more.
7. When finished, suggest they delete or archive the export folder.

## C. Papers into Zotero
Zotero does this; you guide and then verify.
- **Folder of PDFs:** drag the folder into Zotero. It retrieves details for most PDFs automatically. For any left as a standalone PDF, right-click → Create Parent Item and enter the DOI.
- **Mendeley:** Zotero → File → Import → Mendeley Reference Manager (online import). It keeps folders as collections. Sync Mendeley first and spot-check a few annotated papers after.
- **EndNote:** export as EndNote XML or RIS, then Zotero → File → Import. Attach PDFs if the export doesn't bring them.
- **BibTeX/RIS from anywhere else:** File → Import.
Afterwards: check counts against the audit, run Better BibTeX → Pin BibTeX key on everything, then match `inbox/imported-papers.md` against the library. Promote matches (ask before each batch) and leave the rest unverified.

## D. Notes from other apps
- **Notion, OneNote, Evernote, Apple Notes, Google Keep, Bear, and HTML:** use Obsidian's Importer plugin (Settings → Community plugins → Browse → "Importer"). Import into `inbox/imported/<app>/`, then help sort: paper notes → `literature/` only if they match a Zotero citekey (rename to it and fit the template); argument notes → `synthesis/`; admin → `admin/`.
- **Word, PowerPoint, or PDF notes:** convert with Microsoft's open-source MarkItDown, run locally through uv:
  `uvx --from "markitdown[docx,pptx,pdf]" markitdown "<file>" -o "inbox/imported/<name>.md"`
  Ask permission before the first run. Convert a few, check the output with them, then batch.
- **Google Docs:** in Docs, File → Download → Markdown (or .docx, then convert as above).

## E. Drafts
Don't move drafts into the vault. Make a read-only Markdown copy per chapter with MarkItDown into `chapters/<name>.md`, with frontmatter `source: <original path>` and `copy-of: true`, so Claude can search and cite-check them. Tell them to edit the original, and to ask for the copy to be refreshed before a cite-check.

## Finish
Tick the step in `admin/setup-audit.md`, list what needs review (`status: needs-review` files, unverified papers), and add the next step to today's session log.
