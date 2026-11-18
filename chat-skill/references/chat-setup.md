# Set up a research Project in the Claude app

Goal: a Claude Project that holds their notes (not their PDFs), so repeat questions are cheap.

1. Interview with the question tool (multiple choice, plain text if unavailable), one call:
   - "What's your field?" Sciences, Social sciences, Humanities, Health/medicine.
   - "Citation style?" APA 7, Harvard, Chicago author-date, Vancouver/IEEE.
   - "Do you use Zotero yet?" Not installed, Installed but barely used, Use it already.
   - "Do you have an Obsidian vault?" Not yet, Yes.
   Then ask in plain text (optional): thesis question in one sentence, and chapter titles.
2. Write their `CLAUDE.md` with these sections, filled from their answers: What this is (field, question, chapters, style); Finding things (index first, notes second, PDFs last, never a whole PDF to find a reference); Citations (only cite citekeys with notes, `[CITE NEEDED: claim]`, quotes exact with pages, in-text `[@citekey, p. 12]`); Writing notes (template, one index line per note, don't rewrite their prose); Sessions (handoff notes). Tell them to paste it into the Project's instructions and also save it in their vault.
3. If they don't use Zotero, explain in a few sentences: it's free; it stores PDFs and their details; the browser connector saves a paper in one click; it inserts citations and bibliographies into Word or Google Docs in any style; and with the Better BibTeX add-on every paper gets a short stable ID (a citekey) that their notes use as filenames. Link https://www.zotero.org/download and https://retorque.re/zotero-better-bibtex/installation/.
4. If they don't have a vault, explain Obsidian in a few sentences: a free note-taking app where every note is a plain Markdown file in a folder on their computer (the vault), so notes are theirs, work offline, and link to each other with `[[double brackets]]`. Then tell them to download it from https://obsidian.md/download, choose "Create new vault" named `phd-vault`, turn on Settings → Core plugins → Templates, set the template folder to `_templates`, and create these folders: `_index`, `_templates`, `_sessions`, `inbox`, `literature`, `synthesis`, `chapters`, `presentations`, `admin`. Give them the literature-note template and an empty `_index/papers.md` header to paste in.
5. Tell them what to upload to the Project: `CLAUDE.md`, `_index/papers.md`, `_index/themes.md`, and literature notes, not the PDFs. Re-upload the index whenever it changes.
6. Offer to process their first paper with the add-paper workflow.
7. Mention once: if they're happy to install a few things, Claude Code (the Code tab in the Claude desktop app) can read the vault and Zotero directly, which removes the uploading. Point them to the setup guide they were given.
