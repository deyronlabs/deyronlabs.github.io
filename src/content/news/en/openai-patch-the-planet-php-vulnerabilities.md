---
title: "OpenAI says its Patch the Planet coalition helped fix two critical PHP remote-code-execution flaws"
summary: "On 21 October 2026 PHP released 8.5.12, 8.4.27, 8.3.36 and 8.2.35 to fix two critical unauthenticated remote-code-execution vulnerabilities. OpenAI says it led a coalition behind the fix, that Calif found one flaw using GPT-5.6 Sol and that Wiz independently reported both. It also released a version checker."
seoTitle: "PHP critical RCE fixes, found with GPT-5.6 Sol"
seoDescription: "PHP shipped 8.5.12, 8.4.27, 8.3.36 and 8.2.35 on 21 October 2026 to fix two critical RCE flaws; OpenAI says AI helped find them."
lang: en
publishedAt: 2026-10-22T16:50:00Z
entities:
  - OpenAI
  - PHP
  - Calif
  - Wiz
  - GPT-5.6 Sol
topics:
  - Security
  - Research
translationKey: openai-patch-the-planet-php-vulnerabilities
image: /images/news/openai-patch-the-planet-php-vulnerabilities-2026-10-22.jpg
imageAlt: "Deyron Labs graphic: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical remote code execution flaws, CVE-2026-109618 and CVE-2026-109619, CVSS 9.2"
sources:
  - title: "Patch the Planet: global response coordination as agents uncover critical vulnerabilities"
    url: "https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities"
    publisher: "OpenAI"
    primary: true
  - title: "PHP security advisory and releases, 21 October 2026"
    url: "https://www.php.net/index.php"
    publisher: "PHP"
    primary: true
  - title: "php2shell-checker (PHP version checker)"
    url: "https://github.com/openai/php2shell-checker"
    publisher: "OpenAI (GitHub)"
    primary: false
---

## What happened

On 21 October 2026 the PHP project released four patch versions, PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, and said they fix two critical vulnerabilities that can allow unauthenticated remote code execution. The same day OpenAI published "Patch the Planet", saying it led a coalition of maintainers, researchers and security providers for two months to address the flaws, and that frontier AI helped find them.

## Key details

PHP facts are from the project's advisory; the discovery and coordination claims are OpenAI's own.

- **The flaws (PHP advisory):** CVE-2026-109618, described as remote code execution via out-of-memory corruption, and CVE-2026-109619, remote code execution via stale global state. PHP's advance notice rated both 9.2 on CVSS v4.0. The advisory does not name who found them.
- **Fixed versions:** 8.5.12, 8.4.27, 8.3.36 and 8.2.35. PHP also says 8.6.0 RC4 contains the fixes, but marks it as not for production.
- **Mitigations:** if updating is not possible, the advisory lists settings such as `session.upload_progress.enabled=0` and `memory_limit=-1`, and states they "do not make an installation safe".
- **Who found them (OpenAI):** OpenAI says "Calif identified a critical flaw using GPT-5.6 Sol as part of our Patch the Planet initiative, with Wiz also independently discovering and reporting both vulnerabilities". OpenAI's post does not list the CVE numbers.
- **OpenAI's claim:** "To our knowledge, frontier AI found these vulnerabilities before attackers did." We could not verify the absence of earlier exploitation.
- **Tooling and funding (OpenAI):** a PHP version checker, shared as a Codex skill, to help operators identify potentially vulnerable versions (repository name: php2shell-checker), and a commitment of "$1 billion in subsidized Daybreak access" through a programme for frontline defenders. The post also proposes a framework for coordinating responses to AI-discovered flaws.

Checked against both primary pages on 22 October 2026. We did not test the checker or any patched build.

## Why it matters

The practical point for anyone running PHP is to update to a fixed release or confirm that their host has. Unauthenticated remote code execution in a language that runs a large share of websites is the kind of flaw that attackers scan for once a patch is public.

The second point is about process: this is a case where an AI lab says its model contributed to finding a critical flaw and then coordinated disclosure with maintainers. The degree to which the model, rather than the researchers using it, found the bugs is OpenAI's characterisation, and Wiz reported the same issues independently.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic competes with OpenAI, whose claims are reported here. Figures and claims are attributed to their sources.
