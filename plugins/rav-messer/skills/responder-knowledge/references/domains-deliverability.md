# Domains, Custom Domains & Deliverability

Two related topics live here:
1. **Connecting a landing page to your own domain/subdomain.**
2. **Verifying a sending domain & deliverability** (so emails reach the inbox).

## Connect a landing page to a domain / subdomain
**Recommended approach — dedicated subdomain.** Create a subdomain such as
`lp.yourdomain.co.il` and point it at Responder's landing pages. Example: main domain
`cookingschool.co.il` → subdomain `lp.cookingschool.co.il`. You can publish unlimited
pages under one subdomain, and create as many subdomains as you like.
- Publish + set up account subdomain: [offline article catalog](articles/INDEX.md)
- Publish on a private subdomain: [offline article catalog](articles/INDEX.md)

**Publishing on the main/root domain** requires a **WordPress** site on that domain with
the **Ravpage plugin** installed (one-time setup).
- WordPress main-domain publishing: [offline article catalog](articles/INDEX.md)

> General DNS flow: create the subdomain at your DNS provider and point it (CNAME/record)
> as instructed on the publishing screen, then assign the page to that subdomain in
> Responder. Follow the exact target shown in the publish dialog for your account.

## Verify a sending domain (אימות דומיין)
A verified sending domain improves deliverability and trust.
- **Automatic verification** via the Star Communication partnership (fastest for new
  accounts): [offline article](articles/אימות-אוטומטי-של-דומיינים-דרך-שיתוף-הפעולה-עם-סטאר-תקשורת-c4326bda.md)
- **Using a verified private domain for sending:**
  [offline article catalog](articles/INDEX.md)
  and account-side: [offline article](articles/INDEX.md)

## SPF & DKIM
DNS records that authenticate your mail, improve deliverability, and prevent spoofing/
phishing. Add the SPF and DKIM records Responder provides at your DNS host.
- Article: [offline article](articles/מה-זה-spf-ו-dkim-ואיך-הם-קשורים-לשיפור-עבירות-ומניעת-התקפות-פישינג-be97cb39.md)

## Domain warm-up (חימום דומיין)
Gradually increase send volume on a new domain so mailbox providers build trust.
- Article: [offline article](articles/חימום-דומיין-לדיוור-211ea54b.md)

## Deliverability overview (עבירות מייל)
What deliverability is and how to improve it (lists hygiene, content, authentication).
- Article: [offline article](articles/מהי-עבירות-מייל-ואיך-משפרים-אותה-7fd0d8a4.md)
- See also `tips.md`.
