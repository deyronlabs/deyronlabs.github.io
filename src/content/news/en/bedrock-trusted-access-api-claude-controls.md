---
title: "Amazon Bedrock makes its trusted access API generally available and previews Anthropic data controls for Claude models"
summary: "AWS says the Amazon Bedrock trusted access API is generally available and that two Anthropic offerings, Enterprise Frontier Safeguards and Enterprise Data Controls, are in public preview for Claude models. The first keeps retained data in the customer's own S3 bucket; the second uses AWS-managed storage for up to 30 days."
seoTitle: "Bedrock trusted access API and Claude controls"
seoDescription: "AWS made the Amazon Bedrock trusted access API generally available and put two Anthropic data-control options for Claude in preview on 23 Nov 2026."
lang: en
publishedAt: 2026-11-27T07:30:00Z
entities:
  - Amazon Bedrock
  - AWS
  - Anthropic
  - Claude Fable
  - Claude Mythos
  - Enterprise Frontier Safeguards
  - Enterprise Data Controls
topics:
  - Security
  - Enterprise
  - Safety
translationKey: bedrock-trusted-access-api-claude-controls
image: /images/news/bedrock-trusted-access-api-claude-controls.jpg
imageAlt: "Deyron Labs graphic: Amazon Bedrock trusted access API generally available; Anthropic Enterprise Frontier Safeguards and Enterprise Data Controls in public preview; zero data retention exception for Claude Fable through 30 June 2027"
sources:
  - title: "Introducing the Amazon Bedrock Trusted Access API, with Enterprise Frontier Safeguards and Enterprise Data Controls for Claude models"
    url: "https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-trusted-access-api-with-anthropics-enterprise-frontier-safeguards-and-enterprise-data-controls/"
    publisher: "AWS Machine Learning Blog, 23 November 2026 (updated 24 November)"
    primary: true
  - title: "Zero data retention with Enterprise Frontier Safeguards is now in beta"
    url: "https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards"
    publisher: "Anthropic, 23 November 2026"
    primary: false
---

## What happened

On 23 November 2026 AWS published a post saying the Amazon Bedrock trusted access program API is generally available. The API lets customers discover, request and enrol in programs offered by model providers. The same post announces a public preview of two Anthropic offerings for Claude models on Bedrock: Enterprise Frontier Safeguards (EFS) and Enterprise Data Controls (EDC). We read the AWS post on 27 November 2026.

## Key details

All details are from AWS's post. We have not tested either offering.

- **Models covered:** Claude Fable and Claude Mythos, plus Claude Opus 5.5 and Sonnet 5.5 when used through Anthropic's Cyber Verification Program.
- **Enterprise Frontier Safeguards:** retained prompts and completions go to the customer's own Amazon S3 bucket, encrypted with the customer's AWS KMS key. AWS says neither Anthropic nor Bedrock keeps a copy and that AWS human reviewers do not review this content. Bedrock stops serving the covered models 24 hours after it loses access to the key or the bucket.
- **Enterprise Data Controls:** retained data, for up to 30 days, goes to Amazon-managed storage under AWS-managed keys. Human review of flagged cases stays with the customer's team. AWS says cases are not delivered during the preview.
- **Zero data retention exception:** AWS describes an interim exception for current Claude Fable models, for internal use, through at least 30 June 2027.
- **Access and cost:** enrolment goes through the customer's AWS account team, and the preview is for customers already enrolled in EFS zero data retention. Storage settings are per Region. For EFS the post lists the usual S3 and KMS charges; it states no separate price for either offering.

## Why it matters

Companies that want zero data retention and also need providers to monitor for misuse have had to pick one. These options move the question of where retained data lives: in the customer's own bucket and key (EFS) or in AWS-managed storage with a fixed retention window (EDC). The 24-hour shutoff if key access is lost also gives security teams a concrete lever.

This is aimed at enterprise customers, not individual developers, and both offerings are previews with details still to be published, such as pricing for EDC. The claims about data handling are AWS's own description.

> Disclosure: this article is about Claude models made by Anthropic, and Claude was one of the AI tools used to research and draft it, which is a conflict of interest. Deyron Labs is not affiliated with Anthropic or AWS. Earlier coverage of Enterprise Frontier Safeguards: [Anthropic opens Enterprise Frontier Safeguards in public beta](/en/news/anthropic-enterprise-frontier-safeguards-beta/).
