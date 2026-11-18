---
name: audit
description: Take stock of how the person currently works (Claude chats and Projects, where papers and notes live, file formats) and write a migration plan for the vault. Use when they say "audit my setup", "what do I have", "bring my old stuff in", or after setup when they already have existing material.
effort: medium
---

# Audit the current setup

Goal: a clear picture of what exists and where, and a short, ordered plan for bringing the useful parts into the vault. This skill only looks and asks. It never moves, converts, or deletes anything; that's `/phd:migrate`.

## How to ask
Use AskUserQuestion: 1 to 4 questions per call, 2 to 4 options each, multi-select where several can be true. They can always type their own answer. Plain text, one question at a time, if the tool isn't available.

## 1. Interview (two question calls)
First call:
1. "How do you use Claude now?" (multi-select) Chats, Projects, Claude Code, Memory turned on.
2. "Where are your papers?" (multi-select) A folder of PDFs, Zotero, Mendeley, EndNote. (Other: Google Drive, Paperpile, scattered.)
3. "Where are your notes?" (multi-select) Word or Google Docs, Notion, OneNote or Apple Notes, Paper notebooks.
4. "Where are your drafts?" Word, Google Docs, LaTeX/Overleaf, Not started.

Second call, only what applies:
- If they use Projects: "How many Projects relate to the PhD?" 1, 2 to 3, 4 or more.
- If chats: "Roughly how many research chats would be worth keeping?" A handful, Dozens, Lots, No idea.
- "Is anything sensitive (participant data, ethics-restricted material)?" Yes, No, Not sure. If yes or not sure: those files stay where they are and out of the vault and Claude's reach; note it in the plan.
- "Any folders you'd like me to look through?" (free text via Other: paths, or "skip").

## 2. Scan (read-only, with permission)
For each folder they name, ask first, then list without opening files:
- counts by file type (`.pdf`, `.docx`, `.pptx`, `.md`, `.bib`, `.ris`, `.enl`, `.xml`, `.tex`, `.json`, images, others)
- obvious structures: a reference-library export (`.bib`, `.ris`, EndNote `.enl`/`.xml`), a Notion or Evernote export, a `conversations.json` from a Claude export, a LaTeX project
- the 10 most recently changed documents by name and date
Skip system folders, hidden folders, and anything they flagged as sensitive. Don't read file contents in this skill.

If Zotero is connected, also report: number of items, how many have PDFs, how many have notes or annotations, and collections.

## 3. Write the audit
Write `admin/setup-audit.md`:

```
# Setup audit (YYYY-MM-DD)

## What exists
| Source | Where | Size | Format | Bring in? |

## Sensitive, leave in place
## Migration plan
- [ ] 1. ...
## Open questions
```

Order the plan by value per effort, using these defaults:
1. **Research profile first.** Fill `admin/research-profile.md` and the placeholders in `CLAUDE.md` from what they told you. Cheap and makes every later session better.
2. **Papers into Zotero** (if not there yet). Zotero does the heavy lifting: dragging a folder of PDFs in retrieves their details automatically; Mendeley has a direct online import that keeps highlights; EndNote and other managers export RIS or BibTeX for Zotero's File → Import.
3. **Claude Projects and chats**, via the Claude data export: project instructions and files, and research decisions buried in chats.
4. **Notes** from other apps. Notion, OneNote, Evernote, Apple Notes, and Google Keep go through Obsidian's own Importer plugin. Word and Google Docs notes are converted to Markdown.
5. **Drafts stay where they are.** Keep writing in Word, Google Docs, or LaTeX, where the Zotero citation plugins work. The vault gets a read-only Markdown copy for Claude to search, refreshed when needed.
6. **Literature notes only for core papers**, using `/phd:add-paper`. Not for every paper in the library.

Show them the plan, ask which steps to do and in what order with a multi-select question, then offer to start `/phd:migrate` in a fresh session (the audit file carries the plan over). Suggest plan mode for the migration.
