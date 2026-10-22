---
title: "Anthropic releases Claude API version 2026-10-21 with breaking changes and relicensed SDKs"
summary: "On 21 October 2026 Anthropic released Claude API version 2026-10-21, its first new version header listed in the docs. It removes the temperature, top_p and top_k parameters, which now return errors, and ships new major SDK versions under the Apache 2.0 licence instead of MIT."
seoTitle: "Claude API 2026-10-21: removed sampling parameters"
seoDescription: "Claude API version 2026-10-21 removes temperature, top_p and top_k and ships new SDK majors under Apache 2.0, Anthropic said on 21 October 2026."
lang: en
publishedAt: 2026-10-22T17:00:00Z
entities:
  - Anthropic
  - Claude API
topics:
  - Products
  - Coding
translationKey: anthropic-claude-api-version-2026-10-21
image: /images/news/anthropic-claude-api-version-2026-10-21-2026-10-22.jpg
imageAlt: "Deyron Labs graphic: Claude API version 2026-10-21 removes temperature, top_p and top_k, new SDK major versions under Apache 2.0"
sources:
  - title: "Claude API release notes, 21 October 2026"
    url: "https://platform.claude.com/docs/en/release-notes/overview"
    publisher: "Anthropic"
    primary: true
  - title: "API versioning"
    url: "https://platform.claude.com/docs/en/api/versioning"
    publisher: "Anthropic"
    primary: true
  - title: "Migrating to API version 2026-10-21"
    url: "https://platform.claude.com/docs/en/api/migration-2026-10-21"
    publisher: "Anthropic"
    primary: true
---

## What happened

On 21 October 2026 Anthropic's release notes recorded: "We've released API version `2026-10-21`." Developers select an API version with the `anthropic-version` request header, and the versioning page now lists `2026-10-21` with a migration guide. Anthropic makes Claude, the AI tool that helped draft this article, so please read this as a company describing its own changes.

## Key details

Everything below comes from Anthropic's versioning page and release notes, checked on 22 October 2026. We did not read the full migration guide or run any API calls.

- **Messages API changes listed:** a `document` block inside an `assistant` message returns a 400 error; `citations` in a `user` message returns a 400 error; and the `temperature`, `top_p` and `top_k` parameters are removed and "return 400 on every model".
- **Other changes listed:** renamed fields in the Admin API and Enterprise Analytics, and new `enforcement_status` and `enforcement_actions` fields on user profiles.
- **New SDK versions:** Python 2.0.0, TypeScript 1.0.0, C# 13.0.0, Go 2.0.0, Java 3.0.0, PHP 1.0.0, Ruby 2.0.0 and the `ant` CLI 2.0.0.
- **Licence:** the release notes say the SDKs are licensed under Apache 2.0 instead of the MIT License.
- **Older version:** the pages we read list the previous version header (`2023-06-10`) without a deprecation date. A developer newsletter summary says Anthropic plans more frequent versions so teams can handle breaking changes before a new model requires them; we did not find that statement on the pages we read.

## Why it matters

Code that sets `temperature`, `top_p` or `top_k` will fail with errors if it is moved to the new version header, so those calls need removing as part of the upgrade. Nothing in the pages we read says existing integrations on the older header stop working, so the change is something teams can schedule rather than an emergency.

The SDK licence change from MIT to Apache 2.0 matters mostly to companies with open-source compliance rules, because the two licences differ on patent terms and notices. Check the migration guide before upgrading production services.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and this article is about Anthropic. Details are Anthropic's own documentation and have not been independently verified.
