# Sending Emails (שליחת מיילים)

Covers one-off **campaigns** (דיוור / קמפיין). For automatic sequences see
`email-series.md`; for branching flows see `automations.md`.

## What a "regular email / campaign" is
A standard campaign (דיוור רגיל) is sent to one or more lists **immediately or at a
scheduled time** — a newsletter, sale, launch, or invitation. (Series are triggered
automatically per-recipient; campaigns are not.)

**Prerequisite:** at least one list with recipients (see `lists-and-recipients.md`).

## Send a new email campaign (איך שולחים דיוור חדש)
Four stages: choose recipients → name & type → general settings → write content.

1. Click **"דיוורים" / "קמפיינים" (Campaigns)** in the top toolbar — you'll see sent
   and draft campaigns.
2. Click **"דיוור חדש" (New Campaign)** (top-left).
3. Enter an **internal campaign name** (for your own reference), choose **"מייל" (Email)**
   as the method, click **"הבא" (Next)**.
4. **Select recipients:**
   - **By lists:** click **"+ הוסף רשימה" (+ Add List)** — pick one, several, or all
     lists. Duplicates are removed automatically (each recipient gets it once).
   - **Exclude lists:** use the lower **"+ Add List"** to exclude recipients
     (e.g. exclude existing buyers). Exclusions override inclusions.
   - **By conditions (advanced):** target by tenure, past opens/clicks, tags, or stored
     fields — see "advanced recipient settings".
   - The left sidebar shows the live recipient count. Click **"הבא" (Next)**.
5. **General settings:** subject line, tags, sender profile, scheduling (now or later).
6. **Write & design content:** free-write, use a saved template, or duplicate a prior email.
- Article: [offline article](articles/איך-שולחים-דיוור-חדש-d6c370fb.md)

## Send a test email (איך שולחים דיוור ניסיון)
Send the campaign to yourself/colleagues before the real send to check rendering & links.
- Article: [offline article](articles/איך-שולחים-דיוור-נסיון-8456a604.md)

## A/B test (בדיקת נוסח A/B)
Test variants (e.g. subject lines) on part of the list; the winner goes to the rest.
- Article: [offline article](articles/איך-יוצרים-ניסוי-בדיוורים-a-b-test-8768fe4e.md)

When the connected Responder MCP exposes `create_ab_test`, use it to prepare a
standalone campaign draft. Pick `subject` for two or three subjects with one
shared body, or `content` for a separate body per variant. Keep the subject and
preheader identical in content mode when comparing only the bodies. Both modes
use one list and one sender. Pass `sample_percentage` (10–90), `winner_policy`
(`opens` or `clicks`), and a positive `winner_delay` with its unit. The platform
ranks automatic winners by open or click event counts.

Poll `get_async_tool_call_status` for `test_id` and `variant_ids`. Use
`list_ab_tests` to find campaigns and `get_ab_test` to inspect a test, including
a partial draft if creation failed and returned its ID. If the outcome is
uncertain, check the existing drafts before creating another. Use `get_message`
with a variant ID for its preview and message counters.

Use `update_ab_test` with the test ID and only the draft settings that should
change. For example, set `winner_delay: 30` and `winner_delay_unit: "minutes"`
to change the wait. Use `start_ab_test` with the test ID when the user requests
a live launch. It uses the campaign's saved schedule and checks the sample size.
An accepted request can send the automatic winner to the remaining audience.
Check `get_ab_test` for progress. If the launch outcome is uncertain, inspect
the campaign in Responder before taking further action. Use Responder's A/B
testing screen when the connected MCP lacks the update or start tool.

For a series, a Random decision with a different email on each branch gives
a split with manual comparison.

## The editor (עבודה עם העורך)
Same drag-and-drop editor builds forms, templates, landing pages, and emails. Note some
elements/fonts are page-only and not email-safe (see `landing-pages.md`).
- Article: [offline article](articles/עבודה-עם-העורך-ליצירת-טפסים-תבניות-ודפי-נחיתה-826d971f.md)
- Text editor: [offline article](articles/עריכת-דיוור-עם-עורך-הטקסט-bb79f2fe.md)

## Saving a design template for reuse (שמירת תבנית עיצוב)
- Article: [offline article](articles/איך-לשמור-תבנית-בעיצוב-אישי-ולהשתמש-בה-לדיוור-6bf3341e.md)

## Advanced recipient settings (הגדרות נמענים מתקדמות)
Granular targeting by behaviour, tenure, tags and custom fields.
- Article: [offline article](articles/הגדרות-נמענים-מתקדמות-לדיוור-f6c4cc43.md)

## Rename an email / add tags
- Rename: [offline article](articles/איך-משנים-שם-של-דיוור-d7e7857f.md)
- Tags: [offline article](articles/הוספת-תגיות-לדיוור-e6803e34.md)

## Prevent automatic sends on Israeli holidays (מניעת שליחה בחגים)
Exclude specific days (Shabbat / holidays) so scheduled or series sends are skipped.
- Article: [offline article](articles/כיצד-למנוע-שליחה-אוטומטית-של-דיוורים-בחגי-ישראל-a43ea27c.md)
