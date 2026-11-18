# Which skill fits?

Ask what they're trying to do, using the question tool (AskUserQuestion in Claude Code; the multiple-choice question tool in the Claude app; plain text if neither exists). Offer these options, then point to the matching skill and offer to start it:

| They want to | Use |
| :- | :- |
| Start or resume work | `session-start` |
| Save progress mid-way, or the chat feels long | `session-checkpoint` |
| Finish for the day | `session-wrap` |
| Process a new paper | `add-paper` |
| Find a paper or quote they half-remember | `find` |
| Check citations in a draft | `cite-check` |
| Build a presentation or slides | `presentation` |
| Stress-test an argument | `grill` |
| Find new literature on a topic | `lit-search` |
| First-time setup | `setup` |
| See what they have now (chats, Projects, papers, notes) and plan a move | `audit` |
| Bring old chats, Projects, memory, notes or papers into the vault | `migrate` |

In Claude Code the commands are prefixed: `/phd:find`, `/phd:add-paper`, and so on.

## Claude features worth knowing
- **Plan mode** (Claude Code): Claude reads and proposes, but changes nothing until approved. Use it before restructuring notes, batch-processing many papers, or website changes. Shift+Tab cycles to it (Alt+M on some Windows terminals), or start a message with `/plan`.
- **Research** (Claude app): a long multi-source search. Good for mapping an unfamiliar field. Expensive, so not for finding papers already in the vault. Check every source it returns before citing.
- **Question tool**: ask Claude to "interview me with the question tool first" on any big or fuzzy request. A few answers up front beats redoing the work.
- **Models and effort are set for them.** The vault's `.claude/settings.json` uses `opusplan` (Opus while planning in plan mode, Sonnet for everything else) at medium effort. Each kit skill raises or lowers effort while it runs: low for sessions and `find`, high for `cite-check` and `grill`. They don't need to touch either. The one exception is `grill`, which suggests switching to Opus at the start of a fresh session.
- **Switching by hand**: `/model` then press `s` to change the model for this session only; `/effort` to change effort. Switch at the start of a session, not halfway through, because a model switch makes Claude re-read the whole conversation.
- **Claude app**: there's no per-skill setting. Sonnet is the right default; pick Opus from the model menu before starting a new chat for grilling an argument or synthesising across many papers.
