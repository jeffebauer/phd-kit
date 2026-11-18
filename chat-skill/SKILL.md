---
name: phd-research-kit
description: PhD research workflows. Use for literature notes on a paper, finding a half-remembered reference, checking citations in a draft, building a presentation from notes, stress-testing an argument, literature searches, session handoffs, setting up a research Project, and bringing in context from past chats, Projects and memory.
---

# PhD research kit (Claude app)

The person keeps their research notes in an Obsidian vault and their papers in Zotero. In the Claude app you can't see their vault directly: work from this Project's files (usually `CLAUDE.md`, `_index/papers.md`, and a set of literature notes they've uploaded) and from anything they attach or paste.

## Ground rules
- Search the uploaded notes and index before reading any PDF. Never read a whole PDF just to find a reference.
- Only cite citekeys that appear in their notes. Otherwise write `[CITE NEEDED: the claim]`. Never supply a source from memory.
- Quotes need page numbers and must be copied exactly.
- Ask before big or ambiguous work, using the multiple-choice question tool if it's available (2 to 4 options), otherwise plain text, one question at a time.
- The literature-note template is [references/literature-note-template.md](references/literature-note-template.md).
- Output notes as Markdown they can paste into Obsidian, and remind them to re-upload changed index files to the Project.
- Use Australian English.
- Model: Sonnet suits every workflow here except grilling an argument and synthesising across many papers, which are better on Opus. For those, if you aren't Opus, say so at the start and suggest they pick Opus in the model menu and start a new chat; switching mid-conversation is more expensive. Don't nag on other workflows.

## Pick the workflow, then read its file
| The person wants to | Read |
| :- | :- |
| Set up a Project for their research | [references/chat-setup.md](references/chat-setup.md) |
| Take stock of how they work now, or bring in old chats, Projects, notes and papers | [references/audit-and-migrate.md](references/audit-and-migrate.md) |
| Start a session or resume from a handoff | [references/session-start.md](references/session-start.md) |
| Save progress or hand off to a new chat | [references/session-checkpoint.md](references/session-checkpoint.md) |
| Finish a session | [references/session-wrap.md](references/session-wrap.md) |
| Make a note for a paper | [references/add-paper.md](references/add-paper.md) |
| Find a half-remembered reference | [references/find.md](references/find.md) |
| Check citations in a draft | [references/cite-check.md](references/cite-check.md) |
| Build a presentation | [references/presentation.md](references/presentation.md) |
| Stress-test an argument | [references/grill.md](references/grill.md) |
| Find new literature | [references/lit-search.md](references/lit-search.md) |
| Not sure which | [references/guide.md](references/guide.md) |

Where a reference mentions Claude Code, Zotero tools, or file paths in the vault, use the Claude-app fallback it gives instead.
