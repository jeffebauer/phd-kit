---
name: session-checkpoint
description: Save progress mid-session. Use when the person says "checkpoint" or "save progress", before a big change, or when the conversation is getting long.
effort: low
---

# Checkpoint

1. Append to `_sessions/YYYY-MM-DD.md` (today) under `## Checkpoint HH:MM`:
   - Done: notes created or changed, citekeys added
   - Decisions, and why
   - Open questions, including any `[CITE NEEDED]` added
   - Next step, in one sentence
2. Check `_index/papers.md` has a line for every literature note created this session. Add any that are missing.
3. If this conversation is long (many turns, or several papers read), say so plainly and suggest they clear it (`/clear` in Claude Code, or a new chat) and run `session-start`. The log carries everything over, and a fresh session uses far less of their limit.

In the Claude app without a vault: write the checkpoint as a note they can copy, under 20 lines, and suggest they save it to the Project.
