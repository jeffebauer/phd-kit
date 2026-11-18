# Audit and migrate (Claude app)

Goal: find out how the person works now, then pull the useful research context into documents they can save in their vault and their Project. In the Claude app you can't see their computer, so this is lighter than the Claude Code version. Say once, early, that a full migration of a Claude data export is far cheaper in Claude Code, where a script indexes it instead of the conversation reading it.

## 1. Interview
Use the multiple-choice question tool (plain text if unavailable), two calls:
- "How do you use Claude now?" (multi-select) Chats, Projects, Claude Code, Memory on.
- "Where are your papers?" (multi-select) Folder of PDFs, Zotero, Mendeley, EndNote.
- "Where are your notes?" (multi-select) Word or Google Docs, Notion, OneNote or Apple Notes, Paper.
- "Where are your drafts?" Word, Google Docs, LaTeX/Overleaf, Not started.
Then: "Is anything sensitive (participant data, ethics-restricted)?" Yes, No, Not sure. Sensitive material stays out of the vault and out of chats.

## 2. Gather what this chat can reach
- **Past chats:** if you have tools to search or list past conversations, search for their thesis topic, chapter names, and "paper", "literature", "supervisor". Show the titles you found and ask with a multi-select question which to use. If you have no such tools, say that "Search and reference chats" in Settings would let you do this, or that they can paste key chats.
- **Memory:** if memory is on, summarise what you know about their research and ask them to correct it.
- **This Project:** if the chat is inside a Project, read its instructions and files.
Never treat a reference mentioned in a past chat as verified. Past answers can contain wrong or invented citations.

## 3. Produce the documents
Output each as a Markdown block they can copy into Obsidian, with `source: imported from Claude chats` and `status: needs-review` at the top:
1. `admin/research-profile.md`: programme, supervisors, milestones, methods and data, key terms, where drafts live, open questions.
2. Filled-in `CLAUDE.md` details: field, thesis question, chapters, citation style.
3. `synthesis/imported-<theme>.md`: decisions and arguments from past chats, one section per chat with its date.
4. `inbox/imported-papers.md`: papers mentioned, each marked `[UNVERIFIED]` until found in Zotero.
5. `admin/setup-audit.md`: what exists where, and an ordered plan.

## 4. The plan (same order as the Claude Code version)
1. Research profile (done above).
2. Papers into Zotero: drag a PDF folder in (it finds the details); Mendeley via File → Import → Mendeley Reference Manager (online import), which keeps highlights; EndNote via RIS or XML export, then File → Import.
3. Notes from Notion, OneNote, Evernote, Apple Notes, Google Keep: Obsidian's Importer plugin. Google Docs: File → Download → Markdown.
4. Drafts stay in Word, Google Docs, or LaTeX.
5. Literature notes for core papers only, with the add-paper workflow.

## 5. Update the Project and memory
- Suggest new Project instructions (the filled `CLAUDE.md`) and which documents to upload as Project files.
- Suggest 3 to 5 stable facts to save to memory, such as the thesis topic, citation style, and supervisor names, and ask before saving any. Leave out anything sensitive.
