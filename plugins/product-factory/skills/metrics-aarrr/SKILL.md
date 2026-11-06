---
name: metrics-aarrr
description: Use when setting up or reviewing product metrics. Picks one north-star metric per app, one AARRR metric per stage, a weekly review routine and kill or continue rules.
---

# Metrics with AARRR

## Per app
- **North star**: one number for value delivered (for example "weekly active users who finished X").
- **AARRR** (Dave McClure): one primary metric per stage.
  - Acquisition: visitors by channel.
  - Activation: activation event divided by signups.
  - Retention: week-4 return rate.
  - Revenue: paying users and MRR.
  - Referral: invites or shares.
  Prefer rates over totals; totals flatter.
- Name analytics events consistently, for example `<app>:<object>_<action>`, and attach an `app`
  property so several products can share one analytics project.

## Weekly review (about 30 minutes)
Answer three questions: which stage moved, why, and what is the one change to ship this week.
Then propose kill or continue for each app. A starting rule: no activation after 3 weeks live, or
no revenue signal after 6 weeks on a revenue track, means propose archiving the app or moving it
to a portfolio-only track. The owner makes the call; record it in the decision log.

## Daily refresh
Keep it short and automatable.
1. Pull the numbers from their sources (analytics tool, payment provider, repo stats from the
   GitHub API).
2. Write them to one dashboard or data file you control, with the date.
3. Write a three-line brief: what moved, what is failing, decisions waiting.
Log each automated step with a timestamp so a bad number can be traced.

## Sources
- AARRR, Dave McClure (overview): https://www.productcompass.pm/p/aarrr-pirate-metrics
