---
name: idea-validation
description: Use when turning pain-point signals into scored product ideas and deciding Build, Consider or Skip, and whether the idea fits a revenue track or a portfolio (open-source) track.
---

# Idea validation

## Evidence rules (The Mom Test, Rob Fitzpatrick)
- Facts about people's lives beat opinions about your idea.
- Specific past behaviour beats hypothetical futures ("would you use..." tells you nothing).
- Commitment and currency are the signal: time, money or reputation already spent.
  Compliments and "cool idea!" are noise.

## Evidence ladder (strongest last)
complaint, then the same complaint in 3 or more places, then a described workaround
(spreadsheet, assistant, scripts), then paying for a bad tool, then explicitly asking to pay
("take my money", "I'd pay $X").

## Scoring rubric (0 to 5 each, weight in brackets, max 75)
| Criterion | What 5 looks like |
|---|---|
| Pain severity (x3) | costs hours or money every week |
| Breadth (x2) | seen across 3 or more communities, within the last 90 days |
| Money evidence (x3) | people already pay for a worse tool or ask to pay |
| Reachable channel (x2) | a community whose rules allow you to show it |
| Competition gap (x2) | incumbents' 1 to 3 star reviews name the same gap |
| Build appetite (x2) | an MVP fits a 1 to 2 week small batch (Shape Up "appetite") |
| Portfolio value (x1) | showcases a strong skill or can earn GitHub stars |

**Build at 50 or more. Consider at 40 to 49. Skip below 40.** This weighted rubric is a starting
point; adjust the weights to your own situation and keep them fixed across ideas so scores compare.

Track: **Revenue** if money evidence is 3 or more and channel is 3 or more; otherwise
**Portfolio** when portfolio value is 3 or more.

## Output: one brief per idea
Save `research/ideas/<date>-<slug>.md` and add one row to an index file. Include: the problem in
the users' words (quotes and links), who has it, the current workaround, competitors and their
weakest reviews, the score table, the track, the riskiest assumption, and what a cheap test
(landing page, fake door, five interviews) should check.

## Building blocks (portfolio track, fast stars)
Small open-source pieces other builders install: Agent Skills (one `SKILL.md` folder works in
Claude Code, Antigravity, Codex and Copilot), Claude Code plugins and marketplaces, MCP servers,
and self-hostable tools with a one-line Docker start. Score them like any idea, plus:
- Build time of 1 to 3 days; the README demo shows the result in under a minute.
- Demand evidence: requests in r/ClaudeAI, r/ClaudeCode, r/selfhosted, r/LocalLLaMA, GitHub
  issues or discussions ("is there a skill/tool for...", "self-hosted alternative to...").
- A named distribution channel with written rules (plugin marketplace, awesome list, skills
  directory, Show HN, r/selfhosted) and no existing tool that already does it well.

## Kill rules
No quote with a link means no idea. Only one community means Consider at most. Needs paid APIs
that would break your budget cap before any revenue means Skip.

## Sources
- The Mom Test, summary by Michael Lynch: https://mtlynch.io/book-reports/the-mom-test/
- Shape Up, "appetite" (Basecamp): https://basecamp.com/shapeup
