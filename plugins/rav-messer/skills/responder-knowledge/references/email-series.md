# Email Series (סדרות דיוור)

A **series** (סדרה) is a set of pre-written emails sent automatically to each
recipient in a fixed order at scheduled intervals. Two trigger types:
- **Entry-based (כניסה):** starts when a recipient **joins a list**; timing is personal
  to each recipient's signup date.
- **Date-based (תאריך):** sent relative to a **date field** (e.g. birthday) per recipient.

When to use which:
- One-off blast → campaign (`sending-emails.md`).
- Same fixed nurture sequence for everyone who joins → **series**.
- Path depends on behaviour / branching conditions → automation (`automations.md`).

## Create a series manually (איך ליצור סדרת דיוורים)
1. Main menu → **"דיוורים" (Emails)** → **"סדרות" (Series)**.
2. Click **"סדרה חדשה" (New Series)**.
3. Set three basics and confirm:
   - **Series name** (internal).
   - **Trigger** — on entry, or by date.
   - **Target list**.
4. Leave the **main toggle OFF** (top of screen) while you build. Choose whether
   recipients get the series **once** or **repeatedly**.
5. **Gear icon (advanced):** sender profile (legally required), excluded days
   (Shabbat/holidays), default send hour.
6. **Set timing per message:**
   - Entry-based: message 1 relative to signup ("3 hours after"); next messages
     relative to the previous ("3 days after previous").
   - Date-based: **"Edit schedule"** → relative to the date field ("7 days before
     birthday"), pick the hour, choose if it recurs yearly.
7. **"+ ההודעה הבאה בסדרה" (+ Next message)** to add emails; trash icon removes one
   (not the first). Drag the handle to reorder.
8. **"ערוך מייל" (Edit Email)** on each message → duplicate a prior email, use the text
   editor, or pick a template.
9. When ready, switch the **main toggle ON** to activate.

**Important behaviour:**
- Changing a recipient's tenure does **not** move their position (timing = intervals).
- Adding messages to an **active** series affects **new** recipients only, not those
  already in it.
- Unlimited series per list.
- Editing a live series has specific effects — see "impact of changes" below.
- Article: [offline article](articles/יצירה-של-סדרת-דיוורים-56c3ea6d.md)

## Date-based series guide (מדריך לסדרת דיוור לפי תאריך)
- Article: [offline article](articles/מדריך-ליצירת-סדרת-דיוור-לפי-תאריך-adb66092.md)

## Series end / exit element (אלמנט סיום ויציאה מהסדרה)
Lets a recipient exit the series early when a condition is met.
- Article: [offline article](articles/אלמנט-סיום-ויציאה-מהסדרה-32dafb52.md)

## Editing a live series — impact (מה קורה כשמשנים סדרת מסרים קיימת)
- Article: [offline article](articles/השפעה-של-שינויים-בסדרת-דיוורים-קיימת-fe809ceb.md)

## Create a smart series with AI (סדרות דיוור חכמות ב-AI)
**Prerequisite:** complete your **business profile** first so the AI knows your
industry, audience, and values.

Access: top menu **"מערכות נוספות" (Additional Systems)** → **"סדרות AI"** tile.

Three AI series types:
1. **Flexible / custom (גמיש):** write a prompt describing the journey ("abandoned cart:
   reminder after 1h, social proof after 1 day, discount after 2 days"). AI builds the
   framework; adjust timing; click **"צור סדרה בחשבון שלך" (Create series in your account)**.
2. **Challenge (אתגר):** enter a topic ("7-day detox"); AI generates the email skeleton,
   count, and subjects; adjust timing; create.
3. **Gift (מתנה):** describe a lead magnet ("gift series for my PDF guide '…'"), specify
   timing; AI creates subjects; review and create.

After creation: **copy the series between lists**, and **analyze** it (emails sent,
recipients waiting at each step).
- Article: [offline article](articles/יצירת-סדרות-דיוור-חכמות-באמצעות-ai-3992a657.md)
