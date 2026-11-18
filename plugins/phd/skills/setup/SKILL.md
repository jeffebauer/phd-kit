---
name: setup
description: One-time setup for the PhD research kit. Use when the person runs /phd:setup, says "set me up", "get started", or opens a new empty folder they want as their research vault.
effort: medium
---

# PhD kit setup

Goal: in about 20 minutes, leave the person with a working vault, Zotero connected, and one paper processed. Assume they have never used a terminal. Before each step, say in one plain sentence what it does and why. Never run an install command without asking first.

## How to ask
Use the AskUserQuestion tool for every decision and checkpoint: 1 to 4 questions per call, 2 to 4 short options each, recommended option first. The person can always type their own answer. Don't ask what they've already told you. If the tool isn't available, ask in plain text, one question at a time.

For manual steps (installing an app), end with a checkpoint question: "Done", "Stuck", "Skip for now". On "Stuck", ask what they see on screen and help. On "Skip", note it in the session log and move on.

## Step 0: check where we are
- Work out the operating system (try `uname -s`; if that fails or returns MINGW/MSYS, treat it as Windows).
- Look at the current folder. If it already has a `CLAUDE.md` that starts with "# Research vault", ask: repair missing files, or stop. If the folder has unrelated files, ask whether this is the right folder before writing anything.

## Step 1: interview
One AskUserQuestion call:
1. "What's your field?" Options: Sciences, Social sciences, Humanities, Health/medicine.
2. "Where are you in the PhD?" Options: Early (lit review), Middle (research), Writing up.
3. "Which citation style does your department use?" Options: APA 7, Harvard, Chicago author-date, Vancouver/IEEE.
4. "Do you use Zotero yet?" Options: Not installed, Installed but barely used, Use it already.

Then ask in plain text (both optional, "skip" is fine): their thesis question in one sentence, and their chapter titles or working sections.

## Step 2: build the vault
- Copy every file under `${CLAUDE_PLUGIN_ROOT}/vault-template/` into the current folder, keeping the folder structure. Include the hidden `.claude/settings.json`. Use your file tools (read each file, write it), so this works the same on Mac and Windows. Never overwrite a file that already exists.
- Explain the settings file in two sentences: it makes this vault start on `opusplan` (Opus when planning, Sonnet otherwise) at medium effort, and each kit skill adjusts effort while it runs, so they never need to pick a model or effort level by hand. If they're on a plan without Opus, change `model` to `sonnet`.
- In the new `CLAUDE.md`, replace `{{FIELD}}`, `{{QUESTION}}`, `{{CHAPTERS}}` and `{{STYLE}}` with their answers. Use "not set yet" for anything skipped.
- Create `_sessions/YYYY-MM-DD.md` (today's date) with a "Setup" heading. You'll fill it in at the end.
- Show the folder tree and one line on what each folder is for.

## Step 3: Obsidian
Explain in three sentences: Obsidian is a free note-taking app. Every note is a plain Markdown text file in a folder on their computer (Obsidian calls the folder a vault), so the notes are theirs, work offline, and open in any text editor. Notes link to each other with `[[double brackets]]`, which is what lets Claude and they follow a paper's connections; Claude reads the same files directly.

Ask whether Obsidian is installed. If not:
1. Download it from https://obsidian.md/download and install it. Checkpoint.
2. Open Obsidian and choose "Open folder as vault", then pick this folder. (Not "Create new vault", which makes a different folder.) If asked whether to trust the author and enable plugins, "Trust" is fine; the kit adds none. Checkpoint.
3. Set up templates: Settings (bottom-left gear) → Core plugins → turn on Templates. Then Settings → Templates → Template folder location → `_templates`. Checkpoint.
4. Show them three things to try, then ask "Done" / "Stuck":
   - Open `CLAUDE.md` from the left sidebar: it's the instructions Claude follows here, and they can edit it.
   - Quick switcher: Cmd+O (Mac) or Ctrl+O (Windows) to jump to any note by name.
   - Search everything: Cmd+Shift+F or Ctrl+Shift+F.
Mention once: syncing to a phone is optional. Obsidian Sync is paid (students get a discount); keeping the vault on one computer is fine to start.

## Step 4: Zotero (skip parts they already have)
Explain in two sentences what Zotero is for: it stores PDFs and their details, saves papers from the browser in one click, and inserts citations and bibliographies into Word or Google Docs in any style.
1. Install Zotero from https://www.zotero.org/download and the Zotero Connector for their browser (same page). Checkpoint.
2. Install Better BibTeX: download the latest `.xpi` from https://retorque.re/zotero-better-bibtex/installation/ (in Firefox, right-click and save the link). In Zotero: Tools → Plugins → gear icon → Install Plugin From File. Restart Zotero. Checkpoint. Explain: this gives every paper a stable short ID called a citekey, like `smith2024heat`, which the vault uses as filenames.
3. Turn on the local API: Zotero Settings → Advanced → tick "Allow other applications on this computer to communicate with Zotero". Checkpoint.
4. If their library is empty, ask them to save 2 or 3 papers they know well, using the browser connector or Zotero's magic-wand "Add item by identifier" with a DOI. Checkpoint.

## Step 5: connect Claude to Zotero
1. Check `uv --version`. If missing, ask permission, then install:
   - Mac or Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Ask permission, then run `uv tool install zotero-mcp-server` and `uv tool update-shell`.
3. The kit already registers a server called `zotero`. Tell them to quit and reopen Claude Code (or start a new session in the desktop app) so it connects, then run `/phd:setup` again; you'll pick up from here by reading today's session log.
4. Test it with the Zotero search tool: list their 3 most recent items. If it fails, check in order: Zotero is open; the local API box is ticked; `zotero-mcp` runs in a terminal. As a last resort, run `zotero-mcp setup-info` and register the server with `claude mcp add zotero -- <full path it shows>`.
Be clear that this server is open source and community-built, not made by Zotero or Anthropic.

## Step 6: first paper
Ask which of their Zotero papers to start with (offer the recent items as options). Follow `/phd:add-paper` for it. Then show `/phd:find` working on that paper with a vague description, so they see why the notes matter.

## Step 7: finish
- Write today's session log: what was set up, anything skipped, next step.
- Ask with the question tool: "Do you have existing research material to bring in: Claude chats or Projects, notes, a reference library?" Options: Yes, start the audit; Later; No. On yes, suggest a fresh session and `/phd:audit`.
- Show the five commands they'll use most: `/phd:session-start`, `/phd:add-paper`, `/phd:find`, `/phd:session-wrap`, and `/phd:guide` when unsure.
- Remind them: models and effort are handled by the vault settings and the skills, so leave them alone; start a new session per task; and use plan mode (Shift+Tab until it says plan; Alt+M on some Windows terminals) before any change that touches many files.
