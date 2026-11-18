# Research vault: how to work here

## What this is
My PhD research vault. Papers and PDFs live in Zotero. This vault holds my notes about them.

- Field: {{FIELD}}
- Thesis question: {{QUESTION}}
- Chapters: {{CHAPTERS}}
- Citation style for final documents: {{STYLE}}
- More context (supervisors, milestones, methods, key terms, where drafts live): `admin/research-profile.md`. Read it when a task needs that context, not every session.
- Files marked `status: needs-review` were imported and not yet checked. Treat their claims and citations as unverified.

## Finding things (cheapest first)
1. Search `_index/papers.md` (one line per paper).
2. Search `literature/` by citekey, tag, or keyword.
3. Only then use the Zotero tools for annotations or full text.
4. Never open a whole PDF just to find a reference. If steps 1 to 3 fail, say so and ask before going further.

## Citations
- Only cite citekeys that have a note in `literature/`.
- If there's no note, write `[CITE NEEDED: the claim]` instead of guessing a source.
- Quotes need a page number and must come from a literature note or a Zotero annotation. Never put a paraphrase inside quote marks.
- In-text format while drafting: `[@citekey, p. 12]`.

## Writing notes
- New paper notes use `_templates/literature-note.md`. The filename is the citekey.
- Add a line to `_index/papers.md` for every new literature note.
- `synthesis/` and `chapters/` are my own writing. Suggest edits; don't rewrite them.
- Use Australian English.

## Asking me things
- For anything big or ambiguous, ask before starting. Use the question tool with 2 to 4 options where it fits.
- Use plan mode for changes that touch many files.

## Sessions
- At the start, read the newest file in `_sessions/`.
- At the end, append a short summary to today's file in `_sessions/`.
- Skills for this: `/phd:session-start`, `/phd:session-checkpoint`, `/phd:session-wrap`.
