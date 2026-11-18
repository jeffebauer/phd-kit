# Literature search

## 1. Scope
Ask with the question tool (AskUserQuestion in Claude Code; the multiple-choice tool in the Claude app; plain text otherwise):
- "What's the question?" (free text via Other)
- "How wide?" Options: Quick check (5 to 10 papers), Focused scan (10 to 25), Landscape of a field I don't know.
- "Date range?" Options: Last 2 years, Last 5 years, Any.
- "Anything to exclude?" Options: None, Preprints, Non-English, Let me type it.

## 2. Check the vault first
Search `_index/papers.md` and `literature/` so you don't return papers they already have. List what's already covered in a line or two.

## 3. Search
- **Landscape scans in the Claude app:** recommend turning on Research for this one request. Say it uses a lot more of their limit and is worth it only for a field they don't know yet.
- **Otherwise:** use web search. Prefer scholarly sources: publisher pages, DOIs, PubMed, arXiv, OpenAlex, Semantic Scholar, CrossRef.
- Only list a paper you actually saw in a search result or fetched page. Confirm each has a working DOI or publisher URL. Never list a paper from memory.

## 4. Report
Write `inbox/lit-search-YYYY-MM-DD.md` (in the Claude app, output it as text) with a checklist:
`- [ ] Author et al. (year). Title. Journal. DOI · why it's relevant in one line · confidence it's relevant`
Group by sub-theme. End with search terms used and gaps you noticed.

Then tell them how to add the ones they want: in Zotero, the magic-wand "Add item by identifier" button takes a DOI. After that, `add-paper` turns each into a note.
