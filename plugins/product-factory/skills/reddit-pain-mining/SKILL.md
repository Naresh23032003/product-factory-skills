---
name: reddit-pain-mining
description: Use when collecting product-idea signals from Reddit, Hacker News, Product Hunt, GitHub and review sites. Turns public complaints into structured, quoted, linked pain-point signals.
---

# Pain-point mining

Mine complaints instead of brainstorming. Read where people describe problems in their own words,
keep the exact quote and the link, and never pitch anyone.

## Where to look (read-only)
- Reddit: r/SaaS, r/indiehackers, r/microsaas, r/Entrepreneur, r/smallbusiness, r/freelance,
  r/startups, plus 2 or 3 niche subreddits of the target users (for example r/Accounting,
  r/sysadmin, r/Shopify).
- Hacker News: Ask HN threads and Show HN comments ("I'd use this if...").
- Product Hunt: comments on recent launches in the category (missing features, pricing pushback).
- GitHub: issues with many thumbs-up on popular repos, and fast-rising trending repos (unmet
  developer needs).
- Review sites: 1 to 3 star reviews of incumbents on G2, Capterra and app stores (what paying
  users dislike).

### Building-block signals (skills, plugins, MCP servers, self-hosted tools)
r/ClaudeAI, r/ClaudeCode, r/selfhosted, r/LocalLLaMA; GitHub issues and discussions on popular
skills repos and awesome lists. Phrases: "is there a skill for", "MCP server for",
"self-hosted alternative to", "I wish my coding agent could".

## Pain phrases to search for
"alternative to", "wish there was", "is there a tool", "frustrated with", "too expensive",
"doesn't integrate with", "I'd pay for", "switched from", "spreadsheet for", "manually every".

## Classify each signal
pain_type: `pricing`, `missing_feature`, `workflow_friction`, `switching_tool`,
`integration_gap`, `reliability`. Drop launch posts, self-promotion and vague rants.

## Output (one JSON object per signal, at most 30 per run)
```json
{"id":"r-2026-11-07-01","source":"reddit/r/SaaS","url":"...","date":"2026-11-05",
 "quote":"exact words, 40 or fewer","who":"role or segment","pain_type":"workflow_friction",
 "workaround":"what they do today","money_signal":"quote showing payment or willingness, else null",
 "traction":"upvotes/comments"}
```

## Tools and cost
Use free search and page-fetch tools first (a search engine with site filters, `curl`, the
platforms' public JSON or RSS). Never log in, post, vote or send direct messages. Respect
robots.txt and rate limits, and stop at 30 sources per run.

## Exit check
Every signal has a verbatim quote and a working link. No paraphrased "evidence".

## Sources
- Apify Reddit Pain Finder (pain-type classes): https://apify.com/solutionssmart/reddit-pain-finder
- PainPointer (pain phrases): https://painpointer.netlify.app
- Indie Hackers, how to use Reddit to find ideas: https://www.indiehackers.com/post/how-i-use-reddit-to-find-ideas-and-you-can-too-eeb1458853
