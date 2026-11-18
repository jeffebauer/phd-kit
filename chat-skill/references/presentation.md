# Notes to presentation

## 1. Brief
Ask with the question tool (AskUserQuestion in Claude Code; the multiple-choice tool in the Claude app; plain text otherwise), in one call:
- "Who's the audience?" Options: Lab or research group, Conference, Milestone or confirmation panel, General audience.
- "How long?" Options: 5 minutes, 10 to 15 minutes, 20 to 30 minutes, 45+ minutes.
- "What should they leave knowing?" (free text via Other)
- "Which notes should it draw on?" Options: files in `synthesis/`, a chapter, or "Find relevant notes for me".

## 2. Outline (cheap, so iterate here)
Write `presentations/<YYYY-MM-DD>-<short-name>.md`:
- One line per slide: the point it makes, then the citekeys that support it.
- Rule of thumb: about one slide per minute, fewer for a panel.
- Flag any slide whose point has no citation, and any citekey with no literature note.
Ask whether the outline's argument holds before building anything. Offer `grill` if they want it stress-tested.

## 3. Build
When they approve the outline:
- In the Claude app: make the deck with the Slides artifact type if it's available (they can export to PowerPoint or PDF), otherwise a .pptx.
- In Claude Code: add speaker notes to the outline file and offer to build a .pptx, or tell them to paste the outline into the Claude app to make the deck there.
- Final slide: references, formatted in the style from `CLAUDE.md`, generated only from citekeys in the outline.
- Speaker notes: 2 to 4 sentences per slide, in plain spoken language.
