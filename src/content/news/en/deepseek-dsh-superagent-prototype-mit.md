---
title: "DeepSeek team open-sources dsh-superagent, a proactive coding-agent prototype for one GitHub repository"
summary: "A DeepSeek team has published dsh-superagent on GitHub under the MIT license: a research prototype of a proactive coding agent for a single repository, packaged as a bundle for DeepSeek Harness. The repository says it is a prototype for reference only and not an official DeepSeek product."
seoTitle: "DeepSeek dsh-superagent: proactive coding agent"
seoDescription: "DeepSeek's dsh-superagent prototype, open-sourced under MIT around 2 Nov 2026, is a proactive coding agent for one GitHub repo, not an official product."
lang: en
publishedAt: 2026-11-04T00:28:00Z
entities:
  - DeepSeek
  - DeepSeek Harness
  - dsh-superagent
  - GitHub
  - Feishu
topics:
  - Agents
  - Coding
  - Open-weight
  - China
translationKey: deepseek-dsh-superagent-prototype-mit
image: /images/news/deepseek-dsh-superagent-prototype-mit-2026-11-02.jpg
imageAlt: "Deyron Labs graphic: DeepSeek open-sources dsh-superagent, a proactive coding agent for one GitHub repository, MIT license, research prototype and not an official DeepSeek product"
sources:
  - title: "deepseek-ai/dsh-superagent-prototype (GitHub)"
    url: "https://github.com/deepseek-ai/dsh-superagent-prototype"
    publisher: "DeepSeek"
    primary: true
  - title: "DeepSeek team open-sources proactive coding agent research prototype"
    url: "https://technode.com/2026/11/02/deepseek-team-open-sources-proactive-coding-agent-research-prototype/"
    publisher: "TechNode"
---

## What happened

A repository named dsh-superagent-prototype is now public in DeepSeek's GitHub organization. Its description reads "Towards a More Autonomous Agent System", and its readme says "dsh-superagent is a proactive coding agent for one GitHub repository, packaged as a bundle for DeepSeek Harness." TechNode reported the release on 2 November 2026. We could not see a commit date on the repository page.

## Key details

- **License:** MIT.
- **What it does:** the agent listens to events on a GitHub repository and, optionally, to Feishu, rather than waiting for a prompt, and acts on what it finds. Setup instructions are in a SETUP.md file in the repository, and the docs folder includes a philosophy page and a cookbook.
- **Status, in DeepSeek's words:** "Research prototype for reference only, not an official DeepSeek product."
- **Requirements:** it is a bundle for DeepSeek Harness, DeepSeek's open-source agent platform, so it needs that platform to run.
- **Repository figures when we read it:** about 15,900 stars and 1,700 forks, with one commit on the main branch.
- **Not shown:** no benchmarks, no pricing, no model requirements and no description of how it decides when to act.

## Why it matters

Most coding agents wait for a developer to ask. This prototype is built around the opposite idea, an agent that watches a repository and proposes work by itself, and DeepSeek has published the code for others to study and adapt. Because it is labeled a prototype for reference, it is better read as a design example than as a tool to deploy. The high star count shows interest, not quality.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Statements about the prototype are DeepSeek's, read from its GitHub page on 3 November 2026.
