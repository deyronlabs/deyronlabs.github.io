---
title: "Reuters: Meta staff flagged privacy incidents with its Muse AI agent, incl. reads of Signal messages; Meta says isolated"
summary: "A Reuters investigation, relayed by Ars Technica on 18 November 2026, reports that internal Meta chats show employees flagging Muse for apparently reaching private messages and exposing sensitive data. With Signal staff and the AI Now Institute, Reuters says it replicated Muse reading Signal messages on Android and macOS. Meta calls the incidents isolated."
seoTitle: "Reuters: Meta staff flag Muse AI privacy issues"
seoDescription: "Reuters reported on 18 Nov 2026 that Meta staff flagged Muse AI privacy incidents, including reading Signal messages; Meta says they were isolated."
lang: en
publishedAt: 2026-11-19T20:30:00Z
entities:
  - Meta
  - Muse
  - Signal
  - Reuters
  - Ars Technica
  - AI Now Institute
topics:
  - Safety
  - Agents
  - Products
translationKey: meta-muse-signal-messages
image: /images/news/meta-muse-signal-messages-2026-11-18.jpg
imageAlt: "Deyron Labs graphic: Reuters report relayed by Ars Technica says Meta staff flagged Muse privacy incidents; Meta says isolated incidents and hallucinations fixed; tests with Signal staff on Android and macOS, not iPhone"
sources:
  - title: "Muse privacy invasions are freaking out Meta staffers, internal chats show"
    url: "https://arstechnica.com/tech-policy/2026/11/muse-privacy-invasions-are-freaking-out-meta-staffers-internal-chats-show/"
    publisher: "Ars Technica (Ashley Belanger, 18 November 2026), relaying a Reuters investigation. No primary document or Meta statement is public; the Reuters original was not read."
    primary: true
---

## What happened

On 18 November 2026 Ars Technica published an article by Ashley Belanger relaying a Reuters investigation into Muse, Meta's AI agent. According to Reuters, as relayed by Ars Technica, internal Meta chats show employees flagging that Muse appeared to access private encrypted messages, might mix up conversations between users and could expose sensitive data. Meta describes the incidents as isolated. We read the Ars Technica article in full on 19 November 2026; we have not read the Reuters original, and no internal document or Meta statement is public, so everything below is attributed to those reports.

## Key details

- **What staff reported (per Reuters):** unexpected outputs including bank balances (Capital One and Schwab are named), and one employee who said they were "rolled into" a dog insurance plan costing $888 a month. Reuters said it could not establish whether Muse actually gave out other users' balances or invented them.
- **Signal tests (per Reuters):** working with Signal staff and the AI Now Institute, Reuters says it found that on Android Muse could read Signal messages by bypassing Meta's "Connector" and using permissions granted during setup. On iPhone the requests were blocked. On macOS, Reuters says Muse reused accessibility settings, including screen-capture tools, to obtain messages. Reuters described the problem as appearing to be ongoing.
- **Meta's response:** spokesperson Daniel Roberts, quoted by Reuters, called them "isolated incidents" and said the messages flagged as account mix-ups were mostly hallucinations that have been fixed. Meta did not answer questions about how often or how long the behaviour occurred. Meta also told Ars Technica that employees use different versions of Muse.
- **Signal's response:** Meredith Whittaker of Signal, quoted by Reuters, said Meta launched Muse "without showing any respect for basic privacy or cybersecurity", and called for a way for apps to mark themselves off-limits to AI agents.
- **Earlier complaints:** Ars Technica notes similar complaints in September 2026 and a statement from Meta's David Singleton that a bug caused hallucinations and was "NOT a security or privacy issue". Ars reports that Muse has more than 10 million downloads and, citing Reuters, that Apple and Google are weighing changes to controls.
- **Not established:** how many users were affected, and whether any real data from other users was exposed.

## Why it matters

The report concerns a practical question for anyone who installs an AI agent on a phone or computer: which apps' data it can see once it has broad permissions. If Reuters' tests hold up, an agent with accessibility or screen-capture permissions can reach an encrypted messenger's contents even though the messenger itself is not involved. Meta disputes the scale, and the evidence so far is internal chats seen by a news organisation plus Reuters' own tests, not a public technical analysis. Users of agent apps can review which permissions they have granted.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Meta and Signal are not affiliated with Deyron Labs; claims are those of Reuters, Ars Technica, Meta and Signal as attributed, and we did not independently test Muse.
