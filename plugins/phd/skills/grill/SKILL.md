---
name: grill
description: Stress-test an argument like a sceptical examiner, one question at a time. Use when the person says "grill me", "poke holes in this", "prepare me for my milestone/viva", or wants feedback on a chapter's logic.
effort: high
---

# Grill the argument

## 1. Set up
If they named a file or pasted the argument, use it. Otherwise ask with the question tool (AskUserQuestion in Claude Code; the multiple-choice tool in the Claude app; plain text otherwise):
- "What should I grill?" Options: a file in `synthesis/`, a chapter, "I'll paste it".
- "Who should I be?" Options: Supportive supervisor, Sceptical examiner, Reviewer from a rival school of thought, Smart non-specialist.

This works best on Opus. If you aren't running on Opus, say so before the first question and suggest they start a fresh session and switch: in Claude Code type `/model`, choose Opus, and press `s` so it applies to this session only (their default stays put); in the Claude app, pick Opus in the model menu before starting a new chat. Switching at the start of a session is cheap; switching in the middle of a long one makes Claude re-read the whole conversation. If they'd rather not switch, carry on.

## 2. Grill
- Read the argument and the literature notes it cites.
- Ask **one** question at a time. Wait for the answer.
- Target, in rough order: the central claim's clarity, weak or single-source evidence, missing counter-evidence (check `literature/` for notes that disagree), undefined terms, leaps in logic, scope.
- After each answer, say in one line whether it holds, and what changed.
- Point to specific citekeys and pages when you push back. Don't invent counter-evidence; if you suspect a gap in the literature, say it's a suspicion.

## 3. Close
Stop when the argument holds, they say stop, or after about 10 questions. Then write a short summary to the end of the source file under `## Grill notes YYYY-MM-DD` (ask first): what held, what needs work, and evidence to look for.
