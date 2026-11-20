---
title: "Google DeepMind unveils Genie 4, a real-time world model that generates audio, in a trusted-tester preview"
summary: "On 27 October 2026 Google DeepMind announced Genie 4, a world model that generates interactive scenes in real time with audio created alongside the visuals. It is a research preview for trusted testers; DeepMind says it is coming soon to Google AI Ultra subscribers in Project Genie and to early-access partners in the Gemini API and Google AI Studio. DeepMind gives no resolution, frame-rate or benchmark figures."
seoTitle: "Google DeepMind Genie 4 world model preview"
seoDescription: "Google DeepMind announced Genie 4 on 27 October 2026: a real-time world model with native audio, in a trusted-tester preview and a waitlist."
lang: en
publishedAt: 2026-10-27T17:30:00Z
entities:
  - Google DeepMind
  - Genie 4
  - Genie 3
  - Project Genie
  - Gemini Omni
  - Gemini API
  - Google AI Studio
  - SynthID
topics:
  - Models
  - Image generation
  - Research
  - Products
translationKey: google-deepmind-genie-4-world-model-research-preview
image: /images/news/google-deepmind-genie-4-2026-10-27.jpg
imageAlt: "Deyron Labs graphic: Google DeepMind announces Genie 4 on 27 October 2026, a real-time world model with native audio, research preview for trusted testers, Google AI Ultra and API access coming soon, no benchmarks published"
video: https://www.youtube.com/shorts/4WI-M-6SYuI
videoPublishedAt: 2026-10-27T18:05:00Z
updatedAt: 2026-11-20T20:20:00Z
sources:
  - title: "Genie 4 now available through the Gemini API (Google, 19 November 2026)"
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/genie-4-in-gemini-api/"
    publisher: "Google"
    primary: true
  - title: "Genie 4 now available in Project Genie (Google, 18 November 2026; we read only the feed description of this post, not the page)"
    url: "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/"
    publisher: "Google"
    primary: true
  - title: "Genie 4: A new generation of world simulation"
    url: "https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation"
    publisher: "Google DeepMind"
    primary: true
  - title: "Google DeepMind Rolls Out Genie 4 World Model in Research Preview"
    url: "https://www.unite.ai/google-deepmind-rolls-out-genie-4-world-model-in-research-preview/"
    publisher: "Unite.AI"
    primary: false
  - title: "Genie 4 Expands Google's AI Capabilities in Interactive Virtual Environments"
    url: "https://bloomberg.com/news/articles/2026-10-27/google-upgrades-ai-world-model-that-rattled-video-game-stocks"
    publisher: "Bloomberg"
    primary: false
---

## What happened

On 27 October 2026 Google DeepMind announced Genie 4, which it describes as a real-time world model: you move through a generated scene with standard keyboard controls and steer it with text prompts while it runs. DeepMind calls it "natively multimodal" and says it is its first real-time world model to generate audio natively, meaning ambient sound and dialogue are produced together with the visuals.

Genie 4 is a research preview for trusted testers. DeepMind says it is "coming soon" to Google AI Ultra subscribers in Project Genie and to early-access partners in the Gemini API and Google AI Studio, and it links a waitlist.

**Update, 20 November 2026:** the "coming soon" status above has changed. A Google post dated 19 November 2026, which we read in full, says Genie 4 is now available to developers through the Gemini API (the Interactions API) and in Google AI Studio. A separate Google post dated 18 November says Genie 4 is available in Project Genie to eligible Google AI Ultra subscribers; for that one we read only the description in the site's feed, not the page itself.

## Key details

- **Gemini in the loop:** according to DeepMind, Gemini Omni grounds the visuals in how the real world looks and behaves, and other Gemini models help keep scenes coherent. A Gemini model, which the post names as Gemini 3.8 Flash, acts as a guiding agent during generation: it watches frames, breaks a goal into steps and adjusts its plan when the user intervenes.
- **What DeepMind claims:** improved photorealism, more fluid movement and more realistic physics, such as aerodynamics and collisions. These are DeepMind's own descriptions; the post publishes no benchmarks.
- **Not published:** the blog post gives no resolution, frame rate, session length, pricing or list of supported countries. For comparison, Unite.AI reports that Genie 3 ran at 24 frames per second and 720p with consistency lasting a few minutes.
- **Safety:** DeepMind says Genie 4 has safety guardrails, went through internal safety evaluations before the preview, and that all generated video and audio carries SynthID watermarking.
- **Stated limitations:** visual details and object permanence "can still shift or drift over time", especially in long sessions or after several edits. DeepMind also lists complex physical interactions, real-time audio accuracy, legible text, spatial accuracy and long-term consistency as open research areas.
- **Who is testing:** Unite.AI reports that testers in creative industries, journalism, education, gaming and engineering are already evaluating it. Bloomberg's headline links the release to the earlier sell-off in video game stocks that followed Project Genie; we have not independently checked any market movement.
- **Gemini API availability, 19 November (Google):** developers can give Genie 4 a text prompt, a reference image or both. Google says it produces continuous worlds at 720p and 24 frames per second with synchronized native audio (ambient sound, effects and dialogue), that the user steers with keyboard controls in real time and with live text prompts (for example weather, lighting, objects and events), and that "Gemini reasoning" keeps the world consistent. Google lists interactive prototypes, spatial design visualization, and training robots and AI agents as uses. Every output carries an imperceptible SynthID watermark. AI Studio offers an interactive canvas and demo apps.
- **Still not on the page we read:** pricing (the post sends readers to a separate pricing page), rate limits, session length, supported regions, and whether the API access is a preview. The 720p and 24 fps figures are Google's own; we found no independent comparison.

## Why it matters

World models generate an interactive environment rather than a fixed video clip, which is why they interest game developers, simulation and robotics teams, and anyone who prototypes scenes. Adding native audio and a Gemini agent that plans toward a goal moves Genie from a visual demo toward something closer to a playable prototype.

For most readers nothing is available yet: access is limited to trusted testers, the Ultra and API tiers are only "coming soon", and DeepMind offers no measurable quality figures to compare against Genie 3 or other world models. Treat the announcement as a capability preview, and wait for independent hands-on tests of drift, latency and audio quality before drawing conclusions.

The 19 November post moves Genie 4 from the early-access partners DeepMind described in October to availability for developers through the Gemini API and AI Studio. Because pricing and limits are not on the page we read, the cost of running long interactive sessions remains the open question for anyone planning to use it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Google DeepMind is a competitor of Anthropic. All capability claims are DeepMind's unless stated otherwise.
