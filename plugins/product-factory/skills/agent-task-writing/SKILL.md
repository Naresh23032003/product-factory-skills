---
name: agent-task-writing
description: Use when turning a plan or PRD into tasks for a coding agent (Jules, Copilot, Claude Code, Antigravity). Produces self-contained task files that can become GitHub issues.
---

# Writing tasks a coding agent can finish

Issue quality decides whether an agent's PR gets merged. A clear problem, hints about which files
to change and explicit validation criteria are the strongest predictors (Sayagh, "What Makes a
GitHub Issue Ready for Copilot?"; GitHub's coding-agent guidance).

## Rules
- One outcome per task, at most a day of work, ideally 300 changed lines or fewer.
- Self-contained: the agent must not need your chat, the PRD or tribal knowledge.
- Name the files and the existing pattern to copy ("follow `src/lib/billing.ts`").
- Acceptance criteria are observable and testable; include the exact validation commands.
- Say what NOT to touch. Ask for tests with the change.
- Vague verbs ("improve", "clean up", "fix the API") are banned.

## Template (`tasks/NNN-slug.md`)
```
# <imperative title>
## Objective
## Context        (links: PRD story, ADR, related issues)
## Scope          (in / out)
## Files likely touched
## Approach hints (patterns to follow, libraries already in use)
## Acceptance criteria
- [ ] Given ... When ... Then ...
## Validation     (commands that must pass, e.g. `pnpm lint && pnpm test && pnpm e2e`)
## Definition of done (tests added, docs/README updated, screenshot for UI)
```

## Hand-off
Start every task file with front matter: `id: <app>-NNN`, `repo: <owner>/<repo>`,
`status: draft|ready|done`. Turn each `ready` task into exactly one GitHub issue (a small workflow
or script can do it on push; make it idempotent so a task never becomes two issues) and label it
for your agent, for example `jules` or `copilot`, or assign it directly.

Keep one task in flight per area of the code to avoid merge conflicts. Check your agent's free
or paid usage limits and cap the number of tasks dispatched per day to match.

## Sources
- Sayagh, "What Makes a GitHub Issue Ready for Copilot?": https://arxiv.org/abs/2512.21426
- GitHub, getting the best results from the coding agent: https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results
- Jules, running tasks: https://jules.google/docs/running-tasks
- Jules, usage limits: https://jules.google/docs/usage-limits/
