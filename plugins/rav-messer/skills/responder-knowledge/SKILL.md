---
name: responder-knowledge
description: >-
  Answer user questions about the Responder / Rav Messer (רב מסר) email-marketing
  platform and classify a user request to the correct product area. Use this skill
  whenever a user asks how to do something in Responder/Rav Messer — e.g. create an
  email series, send a regular email/campaign, send to a list, create a list or a
  landing page, build a form, set up automation, send SMS, migrate data from the old
  system, connect a landing page to a domain, verify a domain, connect an external
  system (Cardcom, Tranzila, Grow, Zapier, Make, API/webhook), import/export
  recipients, or read statistics. Also use it to triage/route an incoming support
  request to the right feature area.
---

# Responder / Rav Messer Knowledge Base

This skill packages the Responder (Rav Messer / רב מסר) help center into a routed,
searchable knowledge base. The product is an Israeli email-marketing platform; its
UI is **Hebrew**, so reference files include key Hebrew button/label names. Reply to
the user in the language they wrote in (usually Hebrew).

## How to use this skill

You have two jobs. A request usually needs both.

1. **Classify / route** — Read the user request and map it to the correct product
   area using the *Classification Router* below. Name the area back to the user
   ("this is a *Landing Pages* task") so they know where in the product to go.
2. **Explain how to do it** — Open the matching reference file in `references/`,
   then give the user concrete, ordered steps (menu → button → field). Quote the
   Hebrew UI labels where they help. Follow its local article link when the curated
   summary does not contain enough detail.

Workflow:
1. Identify the intent(s) in the request — a request can span several areas
   (e.g. "create a list and a landing page" = Lists + Landing Pages).
2. For each intent, read the relevant `references/*.md` file before answering —
   do not answer product mechanics from memory.
3. Give step-by-step instructions. If something needs a prerequisite (a verified
   domain, a sender profile, a list with recipients), state it first.
4. Use `references/articles/INDEX.md` or search `references/articles/` when the
   topical reference does not answer the question completely. Do not require internet access.
5. Whenever you are creating or editing HTML for a **broadcast/campaign email**
   or a **landing page**, also read `references/responsive-guidelines.md` first
   and apply its rules — this covers the grid/flex min-width overflow trap and
   other mobile-responsiveness pitfalls that aren't obvious from CSS alone.

## Classification Router

Match the user's request to a row. Many requests map to more than one area.

| If the user wants to…                                                  | Product area            | Read this reference                     |
|------------------------------------------------------------------------|-------------------------|-----------------------------------------|
| Send a one-off email / campaign / newsletter to a list                 | Email sending          | `references/sending-emails.md`          |
| Create a regular email / draft / template, A/B test, test email        | Email sending          | `references/sending-emails.md`          |
| Build an automatic email **series** (entry-based or date-based)         | Email series           | `references/email-series.md`            |
| Build a series with **AI** (challenge / gift / custom funnel)           | Email series (AI)      | `references/email-series.md`            |
| Send **SMS**                                                            | SMS                    | `references/sms.md`                     |
| Create / edit / manage a **list**, dynamic list, custom fields          | Lists                  | `references/lists-and-recipients.md`    |
| Add / import / export / move / search **recipients**, statuses, tags    | Recipients             | `references/lists-and-recipients.md`    |
| **Migrate / transfer data** from the old Rav Messer to the new system   | Getting started / migration | `references/getting-started.md`    |
| Create / edit / publish a **landing page**, pop-up, thank-you page      | Landing pages          | `references/landing-pages.md`           |
| Build a landing page with **AI** (HTML/CSS/JS, AI image, AI element)    | Landing pages (AI)     | `references/landing-pages.md`           |
| Create a **form** / signup form, connect a form to a list              | Forms                  | `references/forms.md`                    |
| Connect a landing page to a **domain / subdomain** (DNS, CNAME, WP)     | Domains & deliverability | `references/domains-deliverability.md`|
| **Verify a domain**, SPF/DKIM, warm-up, deliverability, private domain  | Domains & deliverability | `references/domains-deliverability.md`|
| Build an **automation** (trigger → action → condition flow)             | Automations            | `references/automations.md`             |
| Auto-clean lists, dynamic-list-vs-automation, star rating               | Automations            | `references/automations.md`             |
| Connect an **external system** (Cardcom, Tranzila, Grow, Invoice4u, יש חשבונית, תקבול, Kesher CRM, Schooler, Poptin, Webinar Scaling) | Integrations | `references/integrations.md` |
| Connect via **API / webhook / Zapier / Make / Integrately / Boost Space / Zoho Flow** | Integrations | `references/integrations.md`   |
| Install a **plugin/add-on** (WordPress forms, WooCommerce, webinars)    | Integrations           | `references/integrations.md`             |
| View **statistics / reports** (campaign opens, clicks, list stats)      | Statistics             | `references/statistics.md`              |
| **Account settings**, sender profile, add users, block recipients, general settings | Account settings | `references/account-settings.md`  |
| Improve subject lines, deliverability tips, selling with series         | Tips                   | `references/tips.md`                     |
| What changed between versions / new features                            | Version updates        | `references/version-updates.md`         |

### Quick disambiguation
- **"Regular email" vs "series"**: A campaign (דיוור / קמפיין) is sent once, now or
  scheduled. A series (סדרה) is a sequence sent automatically per-recipient, triggered
  by joining a list or by a date field. Automation (אוטומציה) is a branching flow with
  conditions — use it when the path depends on recipient behaviour.
- **"Send to a list"** is the recipient-selection step inside creating a campaign — route
  to `sending-emails.md`, and to `lists-and-recipients.md` if the list doesn't exist yet.
- **Domain**: "connect landing page to a domain" = `domains-deliverability.md` (subdomain/
  WordPress). "Verify a domain so emails deliver" = same file, SPF/DKIM/verification section.
- **List vs dynamic list vs automation**: see the decision note in `references/automations.md`.

## Reference index

- `references/getting-started.md` — Dashboard, moving from the old system, **migrating recipients**.
- `references/sending-emails.md` — Send a campaign, test email, A/B test, editor, templates, scheduling, holiday blocking.
- `references/email-series.md` — Entry-based & date-based series, AI series (challenge/gift/custom), editing live series.
- `references/lists-and-recipients.md` — Create lists (static/dynamic), custom fields, import/export, statuses, tags, "all recipients" list.
- `references/landing-pages.md` — Editor, elements, pop-ups, AI pages, A/B test, thank-you pages, publishing.
- `references/forms.md` — Signup forms, fields, connecting a form to a list, embedding.
- `references/automations.md` — Automation builder, element types, examples, list-cleaning, dynamic-list-vs-automation.
- `references/sms.md` — Sending SMS campaigns, virtual reply number, character limits.
- `references/integrations.md` — API v2, webhooks, payment/CRM/course systems, Zapier/Make, plugins.
- `references/domains-deliverability.md` — Domain verification, SPF/DKIM, warm-up, private domain, subdomain/custom-domain publishing.
- `references/statistics.md` — Campaign reports, list statistics.
- `references/account-settings.md` — Sender profiles, users/permissions, blocking, general settings, content fields.
- `references/tips.md` — Subject lines, deliverability, selling with series.
- `references/version-updates.md` — Release notes.
- `references/responsive-guidelines.md` — Technical CSS reference for building responsive
  HTML (grid/flex min-width overflow trap, embedded third-party widgets/forms). Read this
  whenever generating or editing HTML for a broadcast email or a landing page.

<!-- BEGIN GENERATED OFFLINE ARTICLE INDEX -->
### Offline article corpus (generated)

The complete local corpus contains **151 articles**, refreshed 2026-10-04.
Read `references/articles/INDEX.md` to find an article by category or title, or search
`references/articles/` with `rg`. These files are sufficient for answering without internet access.

- אוטומציות: 7 articles
- דפי נחיתה: 47 articles
- הגדרות החשבון שלך: 10 articles
- חבילות תשלומים מנויים וחשבוניות: 4 articles
- חדשים ברב מסר מתחילים מכאן: 7 articles
- טיפים ונושאים נוספים: 5 articles
- נמענים: 14 articles
- סטטיסטיקה ודוחות: 2 articles
- רב מסר ומערכות חיצוניות: 18 articles
- רשימות: 10 articles
- שליחת sms: 3 articles
- שליחת מיילים: 20 articles
- תוספים של רב מסר: 4 articles
<!-- END GENERATED OFFLINE ARTICLE INDEX -->
