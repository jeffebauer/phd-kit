---
name: find
description: Find a paper, claim, or quote the person half-remembers, searching notes before PDFs. Use when they say "there was a paper that said...", "where did I read...", "find the reference for", or need a citation for a claim.
effort: low
---

# Find that reference

This replaces crawling through PDFs, which is the most expensive thing Claude does in a research workflow.

## 1. Get the clues
If they described it already (including after the command), use that. Otherwise ask with the question tool (AskUserQuestion in Claude Code; the multiple-choice tool in the Claude app; plain text otherwise), up to 3 questions:
- "What do you remember it saying?" (free text via Other)
- "Roughly when was it published?" Options: Last 2 years, 3 to 10 years ago, Older, No idea.
- "Which chapter or theme?" Options from `CLAUDE.md`.

## 2. Search in this order, and stop when you have a strong match
1. `_index/papers.md`
2. `literature/` notes: key claims, quotes, tags
3. `_index/themes.md` and `synthesis/`
4. Zotero annotations and notes (Zotero tools)
5. Zotero full-text or semantic search, but ask first and say it costs more

Never open a whole PDF in this skill. If steps 1 to 4 find nothing, say so, propose a Zotero search query, and wait for a yes.

## 3. Answer
Up to 3 candidates, as a table: citekey, the matching claim or quote, page, where you found it, and confidence (high / medium / low). If the best match comes only from Zotero (no literature note), say so and offer `add-paper` for it.

If nothing matches anywhere, say it plainly. Don't suggest a paper from memory as if it were in their library. If they want new sources, offer `lit-search`.
