---
name: launch-playbook
description: Use when planning or drafting a launch on Hacker News, Reddit, Product Hunt or GitHub. Covers each community's written rules; every public post stays a draft until the owner approves it.
---

# Launch playbook

## Hacker News: Show HN (official rules)
- Only for things people can try now. Landing pages, sign-up pages and blog posts are not Show HNs.
- Title: `Show HN: <Name> - <what it does, plainly>`. No hype, caps or exclamation marks.
- The maker posts and stays in the thread answering questions. Never ask anyone for upvotes.

## Reddit
- Read each subreddit's sidebar rules first. Many allow promotion only on set days or threads
  (for example a weekly self-promotion or showoff day).
- Participate before posting and keep promotion a small share of your activity (roughly 90/10).
- Lead with the problem and what you learned, disclose that you built it, and post to one
  subreddit per day.

## Product Hunt
Launch at 12:01 AM Pacific, Tuesday to Thursday. Write a tagline that is understandable in 5
seconds, prepare a gallery and demo video and the first maker comment, and reply to every comment
quickly.

## GitHub stars (open-source projects)
README with a demo GIF first (see `readme-and-demo`), then Show HN, then relevant awesome lists,
then good-first-issues.

## Building blocks (skills, plugins, MCP servers, self-hosted tools)
Ship the repo installable in one line: `/plugin marketplace add <owner>/<repo>` for Claude Code
(backed by a `.claude-plugin/marketplace.json`), the same `skills/<name>/SKILL.md` folder copied to
`.agents/skills/` for Antigravity, and `docker compose up -d` for self-hosted tools. Then submit to
the relevant awesome list or directory following its CONTRIBUTING rules (one PR, no duplicates),
and post once where the audience is (r/ClaudeAI, r/selfhosted, Show HN) on a day the subreddit
allows self-promotion.

## Every launch
- Keep drafts in the repo, one file per channel, with the community rule quoted next to the draft.
- Use UTM-tagged links so your analytics show which channel worked.
- Log each post in a decision log and get the owner's explicit approval before it goes out.
- No vote solicitation, no sockpuppet accounts, no mass posting.

## Sources
- Show HN rules: https://news.ycombinator.com/showhn.html
- Hacker News guidelines: https://news.ycombinator.com/newsguidelines.html
- Indie Hackers, subreddit unwritten rules: https://www.indiehackers.com/post/every-subreddit-has-different-unwritten-rules-and-heres-how-to-decode-them-before-posting-1wSck8RGykjDv4FAwS69
- Product Hunt launch checklist: https://gingiris.github.io/growth-tools/blog/2026/03/29/product-hunt-launch-checklist-the-complete-2026-guide-from-30x-daily-1-experience/
- Claude Code plugin marketplaces: https://code.claude.com/docs/en/plugin-marketplaces
- Antigravity skills: https://antigravity.google/docs/skills
