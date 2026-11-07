---
title: "OpenAI introduces BioBasicsBench: GPT-6 Astra scores 66.7% on 100 everyday wet-lab data tasks"
summary: "On 6 November 2026 OpenAI published BioBasicsBench, built with Ligo: 100 tasks that ask AI agents to interpret raw lab data such as gels, colony plates and microscopy. At the highest effort setting, GPT-6 Astra scored 66.7%, against 43.8% for GPT-5.6 Sol. OpenAI says higher scores do not yet mean reliable judgment in a real lab."
seoTitle: "OpenAI BioBasicsBench: GPT-6 Astra scores 66.7%"
seoDescription: "OpenAI's BioBasicsBench, published 6 Nov 2026 with Ligo, tests agents on 100 wet-lab data tasks; GPT-6 Astra scored 66.7% at xhigh, per OpenAI."
lang: en
publishedAt: 2026-11-07T09:00:00Z
entities:
  - OpenAI
  - Ligo
  - BioBasicsBench
  - GPT-6 Astra
  - GPT-6.1 Sol
  - GPT-5.6 Sol
topics:
  - Research
  - Science
translationKey: openai-wet-lab-agents
image: /images/news/openai-wet-lab-agents-2026-11-06.jpg
imageAlt: "Deyron Labs graphic: OpenAI's BioBasicsBench has 100 wet-lab data tasks; GPT-6 Astra scores 66.7% at xhigh effort, GPT-5.6 Sol 43.8%, per OpenAI's own test"
sources:
  - title: "Measuring how AI agents handle everyday wet-lab science"
    url: "https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science/"
    publisher: "OpenAI"
    primary: true
---

## What happened

On 6 November 2026, OpenAI published "Measuring how AI agents handle everyday wet-lab science", introducing a benchmark called **BioBasicsBench**. OpenAI developed it with Ligo, a biotechnology company that works on enzyme design. It is an evaluation, not a product launch.

The benchmark has 100 tasks in which an AI agent has to interpret raw data from "wet" laboratory work: gels, plates with bacterial colonies, microscopy images, instrument readouts and similar material. The tasks are spread over five areas: protein methods, imaging and cytometry, quantification and assays, nucleic acid methods, and molecular cloning. OpenAI says each task was reviewed internally by Ligo, externally by a scientist with a PhD, and then internally again.

## Key details

- **Models tested (all OpenAI's):** GPT-5.2, GPT-5.4, GPT-5.5, GPT-5.6 Sol, GPT-6.1 Sol, GPT-6 Luna and GPT-6 Astra, across 37 model and effort settings. With five attempts on each of the 100 tasks, that gives 18,500 results.
- **Scores at the highest ("xhigh") effort setting, per OpenAI:** GPT-6 Astra 66.7% (95% confidence interval 60.3% to 73.1%), GPT-6.1 Sol 62.0%, GPT-5.6 Sol 43.8%, GPT-6 Luna 38.3%, GPT-5.5 35.4%, GPT-5.4 33.2% and GPT-5.2 31.2%.
- **Cost of answering:** OpenAI reports that GPT-6 Astra used about 4,704 output tokens per task, against 9,099 for GPT-5.6 Sol.
- **What the tasks look like:** 31 gels or blots, 27 protocols or notes, 20 tables or exports, 18 bench photos, 14 microscopy images, 13 instrument screens, 12 sequencing files, 7 videos and 7 colony plates.
- **Where the best model fails (OpenAI's examples):** on one colony-plate task, GPT-6 Astra picked colonies 4, 6, 7 and 8 where the reference answer was 5, 9 and 10. In another, it generalized about "darker vacuoles" and ignored the brightest ones. OpenAI also reports that it overcounts colonies by about 12%.
- **OpenAI's own caveat:** "Higher benchmark scores do not yet mean models can make reliable judgments in the lab."
- **What the page does not say:** we found no statement on whether the benchmark or its data are public, and the only models compared are OpenAI's own. No other lab's models were evaluated.

All figures are OpenAI's, from the page published on 6 November 2026, which we read on 7 November.

## Why it matters

Reading lab data is routine, unglamorous work, and it is a more concrete test of "AI for science" than answering exam-style biology questions. The gap OpenAI reports between older and newer models, from 31.2% to 66.7% at the top effort setting, shows how quickly this particular skill is improving on its own measure.

Still, a score of two out of three is not the same as a tool a lab can rely on. The failures OpenAI describes, such as picking the wrong colonies, are the kind a researcher would have to catch by checking the result themselves. Because OpenAI built the test and evaluated only its own models, there is no independent number to compare against, and we cannot say how other labs' models would score. Treat BioBasicsBench as a useful description of what current agents can and cannot do at the bench, not as proof they can replace a trained scientist.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. All figures are OpenAI's unless stated otherwise.
