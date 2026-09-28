# Getting Started & Migration (חדשים ברב מסר? מתחילים מכאן)

Onboarding for new users and moving from the **old** Rav Messer system to the **new** one.

## The Dashboard (המסך הראשי – הדשבורד)
The dashboard is the home screen after login: primary navigation, an overview of
account activity, and entry points to campaigns, lists, pages, and automations.
- Article: [offline article](articles/המסך-הראשי-הדשבורד-155f40bf.md)

## Moving from the old system (על המעבר מהמערכת הקודמת)
The new platform has a **different list structure** — your old lists do not carry
over automatically, so newly created lists start empty. Review what changed before
migrating.
- Article: [offline article](articles/מה-צריך-לדעת-במעבר-למערכת-החדשה-50bc5b8f.md)

## Migrating recipients: old → new (העברת נמענים מהמערכת הישנה לחדשה)

There are **two migration methods**:

### Method 1 — Export / Import via CSV (best for static, finished lists)
1. In the **old** Rav Messer, export the recipient list to a **CSV** file.
2. (Optional) Open/clean the file in Excel or Google Sheets.
3. In the **new** system, import the CSV into the target list (see
   `lists-and-recipients.md` → Importing recipients).
4. During import, **map each old field** to the new field.

**Field-mapping notes:**
- **Names:** the old system used one "name" field; the new one uses separate
  first/last name. Map the old "name" to **"Full name" (שם מלא)** and the system
  splits on the first space ("David Ben-Gurion" → first "David", last "Ben-Gurion").
- **Status:** old "active/inactive" values sync automatically — no manual fix needed.

### Method 2 — Automation tools (best for ongoing sync)
Use **Zapier** or **Make (Integromat)** to keep both systems in sync — e.g. when the
old system still hosts live landing pages but the new system runs the automations.
See `integrations.md`.

**Routing tip:** "transfer my contacts / data from the old רב מסר" → Method 1.
"keep the old system and the new one synced" → Method 2.

- Article: [offline article](articles/העברת-נמענים-ממערכת-רב-מסר-הישנה-לחדשה-111d012e.md)

## Automatic domain verification (אימות אוטומטי של דומיינים)
New accounts can auto-verify a sending domain via the Star Communication partnership.
See `domains-deliverability.md`.
- Article: [offline article](articles/אימות-אוטומטי-של-דומיינים-דרך-שיתוף-הפעולה-עם-סטאר-תקשורת-c4326bda.md)
