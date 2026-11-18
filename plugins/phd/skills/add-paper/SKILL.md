---
name: add-paper
description: Turn a paper into a literature note so it never needs re-reading. Use when the person says "add this paper", "make a note for", "I just read", shares a PDF, or names a citekey or Zotero item to process.
effort: medium
---

# Add a paper

The point: read a paper once, record what matters with page numbers, and never reopen the PDF just to find something.

## 1. Identify the paper
If they named a citekey, title, or DOI (including after the command), use it. Otherwise ask with the question tool (AskUserQuestion in Claude Code; the multiple-choice tool in the Claude app; plain text otherwise), offering their 3 most recent Zotero items as options if the Zotero tools are connected.

Then ask, in the same question call:
- "How deep?" Options: Quick (takeaway + 3 claims), Standard (full template), Core paper (full template + detailed method notes).
- "Which chapters does it relate to?" Options from the chapter list in `CLAUDE.md`, multi-select allowed.

## 2. Gather, cheapest first
1. Zotero metadata (title, authors, year, DOI, citekey).
2. Their Zotero annotations and highlights, with page numbers. These show what they thought mattered.
3. Only then the PDF full text, and only for gaps the annotations don't cover.
In the Claude app: use the PDF they attached. Ask for the citekey if they use Zotero; otherwise build one as `firstauthorYEARfirstword` in lower case.

## 3. Write the note
- Use `_templates/literature-note.md`. Save as `literature/<citekey>.md`. If the file exists, ask before changing it.
- Every claim gets a page number. Copy quotes exactly; never put a paraphrase inside quote marks. If you can't find the page, write `(p. ?)` rather than guess.
- In "How it connects", link only citekeys that already have notes. Mention other relevant papers in plain text with "(no note yet)".
- Leave the one-line takeaway as your draft and ask them to rewrite it in their own words. That line is what makes it stick.

## 4. Index it
Add one line to `_index/papers.md`: `- [[citekey]] · year · what it found, in a few specific words · #chapter tags`. Specific beats general: "survey n=1,200, symptoms above 35°C" finds better than "heat stress paper".

In the Claude app without a vault: output the note and the index line as text for them to save in Obsidian, and remind them to re-upload the index to their Project.

## Batch mode
If they want several papers processed, suggest plan mode first, process them one at a time, and run `session-checkpoint` every 5 papers. Haiku or Sonnet is plenty for this.
