# PhD research kit for Claude

A small set of skills for doing PhD research with Claude without burning through your usage. The idea: read each paper once, write down what matters with page numbers, and have Claude search those notes instead of re-reading PDFs.

- **Zotero** holds your papers, PDFs, and highlights.
- **Obsidian** holds your notes, as plain Markdown files in a folder (the vault).
- **Claude** searches the notes first, Zotero second, and only cites papers you have notes for.

## Install

### Option A: Claude Code (recommended)

Uses the Code tab in the Claude desktop app, or the `claude` command in a terminal.

1. Make an empty folder called `phd-vault` in your Documents folder.
2. Open that folder in Claude Code.
3. Type these one at a time:

   ```
   /plugin marketplace add jeffebauer/phd-kit
   /plugin install phd@phd-kit
   ```

   If `/plugin` isn't recognised, run the same thing in a terminal instead: `claude plugin marketplace add jeffebauer/phd-kit`, then `claude plugin install phd@phd-kit`.
4. Start a new session in the same folder and type `/phd:setup`. It interviews you, builds the vault, and walks you through Obsidian, Zotero, and connecting the two. About 20 minutes.

Updates: `/plugin marketplace update phd-kit`.

### Option B: Claude app only (no installs)

1. Download `dist/phd-research-kit.zip`.
2. In Claude: Settings → Capabilities, make sure code execution / file creation is on.
3. Customize → Skills → **+** → Create skill → Upload a skill → choose the zip.
4. Create a Project for your thesis and say: "Use the PhD research kit to set up this Project."

Pick one option. Skills uploaded to the Claude app also load in Claude Code, so installing both gives you duplicates.

## Skills

| Command (Claude Code) | What it does |
| :- | :- |
| `/phd:setup` | One-time interactive setup |
| `/phd:guide` | Which skill fits what you're doing |
| `/phd:audit` | Takes stock of chats, Projects, papers, notes and formats; writes a migration plan |
| `/phd:migrate` | Brings in Claude export (chats, Projects, memory), papers, notes, and draft copies |
| `/phd:session-start` | Resume from the last session log |
| `/phd:session-checkpoint` | Save progress; suggests a fresh session when the chat gets long |
| `/phd:session-wrap` | End-of-day log, CITE NEEDED list, supervisor notes |
| `/phd:add-paper` | Paper → literature note with page-anchored claims, plus an index line |
| `/phd:find` | Half-remembered reference → citekey and page, notes before PDFs |
| `/phd:cite-check` | Verify every citation and quote in a draft |
| `/phd:presentation` | Notes → outline → slides with speaker notes and references |
| `/phd:grill` | Sceptical-examiner questions, one at a time |
| `/phd:lit-search` | New literature, verified DOIs only, into `inbox/` |

In the Claude app, ask in plain words ("find the paper that said...") and the kit picks the workflow.

## Zotero connection

The plugin registers the open-source [zotero-mcp](https://github.com/54yyyu/zotero-mcp) server. It's community-built, not made by Zotero or Anthropic. `/phd:setup` installs it with `uv tool install zotero-mcp-server` and checks it works. It needs Zotero open with the local API turned on.

## Maintaining this repo

- Skills live in `plugins/phd/skills/`. Edit there only.
- Rebuild the Claude app zip after any skill change: `python3 scripts/build-chat-skill.py`.
- Bump `version` in `plugins/phd/.claude-plugin/plugin.json` when you push changes, or users stay on the old version.
- Check before pushing: `claude plugin validate .` and `claude plugin validate plugins/phd`.
- Plugin skills may use Claude Code-only frontmatter such as `effort`. The build script strips frontmatter when it copies them into the chat bundle, and the chat bundle's own `SKILL.md` keeps to `name` and `description`, because the Claude app rejects other keys on upload.

## Models and effort

- The vault template ships `.claude/settings.json` with `"model": "opusplan"` (Opus in plan mode, Sonnet otherwise) and `"effortLevel": "medium"`.
- Each skill sets `effort` in its frontmatter, which applies only while that skill runs: low for `guide`, `find`, and the session skills; medium for `setup`, `add-paper`, `presentation`, and `lit-search`; high for `cite-check` and `grill`.
- Skills deliberately don't set `model`. Switching models mid-conversation makes Claude re-read the whole conversation without the cache, which costs more than it saves. `grill` suggests switching to Opus at the start of a fresh session instead.

MIT licence.
