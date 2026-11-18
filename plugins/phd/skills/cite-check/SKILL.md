---
name: cite-check
description: Check every citation and quote in a draft against the vault and Zotero. Use when the person says "check my citations", "verify references", or before sending a chapter, paper, or slides to a supervisor.
effort: high
---

# Citation check

## 1. What to check
If they named a file or pasted text, use it. Otherwise ask with the question tool (AskUserQuestion in Claude Code; the multiple-choice tool in the Claude app; plain text otherwise) which file in `chapters/`, `synthesis/` or `presentations/` to check, offering the most recently changed files.

## 2. For each citation
1. Does the citekey have a note in `literature/`? If not, does it exist in Zotero?
2. Does the claim in the draft match what the note says, on that page?
3. For direct quotes: does the text match the note or Zotero annotation word for word, with the right page?
4. Is there an uncited factual claim that needs a source? Mark it.

## 3. Report
A table: location in the draft, citekey, status (OK / mismatch / no note / not in Zotero / quote differs / needs citation), and a one-line fix. Put problems first.

Don't rewrite their prose. Offer to insert `[CITE NEEDED: ...]` markers if they want them in the file.

Never "fix" a missing source by supplying one from memory. If they want help finding one, offer `find` (their library) or `lit-search` (new sources).
