---
title: "Replit launches Missions: budget-capped swarms of coding agents, with results Replit measured itself"
summary: "On 17 November 2026 Replit introduced Missions, which has a user set an outcome, a budget and permissions, then coordinates a swarm of agents to plan, build and test it, with an AI judge checking the result. Replit's own tests, including a comparison with Claude Code, are the only evidence so far."
seoTitle: "Replit Missions: budget-capped agent swarms"
seoDescription: "Replit's Missions, launched 17 Nov 2026, runs swarms of coding agents within a user-set budget; the benchmark figures are Replit's own tests."
lang: en
publishedAt: 2026-11-18T19:05:00Z
entities:
  - Replit
  - Replit Missions
  - DataCat
  - Claude Code
  - NumPy
topics:
  - Products
  - Agents
  - Coding
translationKey: replit-missions
image: /images/news/replit-missions-2026-11-17.jpg
imageAlt: "Deyron Labs graphic: Replit Missions, 17 Nov 2026; agent swarms within a set budget; DataCat built in 2 days under a 3,000 dollar cap; NumPy speedups up to 19x with 32 agents; all figures are Replit's own tests"
sources:
  - title: "Introducing Replit Missions"
    url: "https://replit.com/blog/introducing-replit-missions"
    publisher: "Replit, 17 November 2026"
    primary: true
---

## What happened

On 17 November 2026 Replit published "Introducing Replit Missions". According to the post, a user defines an outcome and Replit coordinates a swarm of agents that plan, build, test and iterate on it inside a budget and a set of permissions the user agrees to up front (Replit calls this the Missions agreement). An independent AI judge checks the results against the agreed criteria. If the budget runs out first, the work stops and the result is reported as unresolved. Missions run in the cloud, and the user chooses whether to be notified immediately, in a daily digest or in a weekly one. We read the full Replit post on 18 November 2026.

## Key details

- **How to start:** the post says to click New, then Mission. It does not list prices, plan eligibility or availability by region, and we found none on the pages we read.
- **DataCat example:** Replit says it built DataCat, an application-monitoring platform, with Missions in two days under a 3,000 USD budget cap. It reports an alert within 38 seconds of a deliberately introduced database bug (target: 60 seconds), and a three-hour test with 26 million activity records and 4.4 million log entries and no losses. It also reports 51 of 51 checks passed on data accuracy and alert reliability.
- **Against the original platform:** on tasks Replit describes as suitable for Node.js, it reports 39% more requests processed and 51% less CPU overhead for monitoring than the original platform's agent, agent memory of 82 to 108 MB against 319 MB, and logs searchable in 0.5 seconds against 4.2. The post does not name the original platform.
- **Against Claude Code:** Replit compared DataCat with a version built from the same initial prompt using Claude Code's /goal. It reports API compatibility of 51/56 against 45/56 and 49,000 against 9,800 traces per second (about 5x). It also says the Claude Code build covered more product areas and ingested logs faster. Each variant was run once.
- **NumPy:** on 13 tasks, Replit reports speedups of up to 4x with one agent, 17x with a swarm of 16 and 19x with 32 on its Auto (Max) setting, and 2x, 7x and 9x on Auto (Power).
- **E-Commerce Bench:** Replit reports a score rising from ¥100,000 to ¥4.82 million (about 48x) and calls it state of the art, more than three times the best on the public leaderboard. That characterisation is Replit's.
- **Open source:** Replit says it is releasing a self-hostable version of DataCat. We did not read the repository or its licence.
- **Caveats from the post:** Replit states that its controlled tests do not establish performance against the original hosted service, or on Replit's production systems, and that each setup was run once.

## Why it matters

Missions is a bet that long coding jobs should be run as budgeted projects with an automated check at the end, not as a single chat session. The idea is concrete: a spending cap and a judge give a user a defined stopping point. What is missing is independent evidence. Every figure above comes from Replit's own tests, one run per variant, in a comparison against a competitor's product, and the judge's method and the pricing are not described. Treat the numbers as Replit's claims until outside users reproduce them.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Replit compares its results with Anthropic's Claude Code, so Anthropic has an interest in this story. Replit is not affiliated with Deyron Labs; all figures are Replit's own.
