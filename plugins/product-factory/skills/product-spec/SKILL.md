---
name: product-spec
description: Use when writing the spec for an approved idea. Produces an Amazon Working Backwards PR/FAQ, then a Shape Up pitch, then a PRD with testable Gherkin acceptance criteria.
---

# Product spec

Three documents, in this order. If the press release is not compelling, stop: the idea is not
ready.

## 1. PR/FAQ (Working Backwards, Bryar and Carr)
- One-page press release written for the customer and dated launch day: headline, sub-headline
  (who and the benefit), problem, solution, a customer quote, how to get started.
- FAQ, external first (customers: price, how it works, what it does not do), then internal (cost,
  risks, dependencies, why now, how you will know it worked).

## 2. Pitch (Shape Up, Basecamp)
Five parts: **Problem**, **Appetite** (a small batch of 1 to 2 weeks by default; time is fixed,
scope flexes), **Solution** (breadboard or fat-marker level, not pixels), **Rabbit holes** (risks
and how you patch them), **No-gos** (what you deliberately will not do).

## 3. PRD
- Users and jobs to be done; the one **north-star metric** and the activation event.
- User stories, each with Gherkin acceptance criteria:
  `Given <context> When <action> Then <observable result>`.
- Non-functional requirements: performance budget, accessibility (WCAG 2.2 AA), and a security
  level (OWASP ASVS Level 1 as the floor for anything that takes payments or stores user data).
- Analytics events to instrument, with a consistent naming scheme such as
  `<app>:<object>_<action>`, every event tagged with the app name.
- If the product charges money: pricing, plan limits and the payment provider.
- Out of scope (copy the No-gos).

## Exit check
Every story has acceptance criteria a test can check. Appetite and No-gos are explicit. Nothing
in the PRD needs a paid service outside your budget cap.

## Sources
- Working Backwards PR/FAQ: https://workingbackwards.com/resources/working-backwards-pr-faq/
- Product management at Amazon (AWS): https://aws.amazon.com/executive-insights/content/product-management-at-amazon/
- Shape Up (Basecamp): https://basecamp.com/shapeup
- Gherkin reference: https://cucumber.io/docs/gherkin/reference/
