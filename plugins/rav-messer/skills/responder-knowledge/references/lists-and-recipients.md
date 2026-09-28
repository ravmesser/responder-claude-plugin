# Lists & Recipients (רשימות ונמענים)

Lists hold recipients. Recipients are the people. Most "send to X" tasks start here.

## Create a new list (יצירת רשימת נמענים חדשה)
1. Main recipient-lists screen → **"רשימה חדשה" (New List)**.
2. Fill the settings:
   - **Hidden/internal name** (שם פנימי) — how you find it; pick something clear
     ("Launch Event 22/6", not cryptic).
   - **Public name** (שם פומבי) — shown to recipients (e.g. on unsubscribe pages).
   - **Tags** — to find/group the list later.
   - **Sender profile** — default sender (full sender details are legally required;
     can be overridden per campaign).
   - **Join/leave notification email** — get notified on subscribe/unsubscribe.
   - **Double opt-in** — require email confirmation before joining.
   - **Dynamic list** — auto-updating list by criteria (see below).
3. Click **"צור רשימה חדשה" (Create New List)**.
4. The list is empty — add recipients manually, by import, or via a signup form.
- Article: [offline article](articles/איך-יוצרים-רשימת-נמענים-חדשה-848addff.md)

## Static vs dynamic list (מה ההבדל בין רשימה רגילה לדינמית)
- **Static/regular:** you add/remove recipients manually or by import.
- **Dynamic:** membership is computed automatically from rules (tags, fields,
  behaviour). Recipients move in/out as they match. Compare with automations in
  `automations.md`.
- Difference: [offline article](articles/מה-ההבדל-בין-רשימה-רגילה-לרשימה-דינמית-0f26f7ab.md)
- Create dynamic list: [offline article](articles/איך-ליצור-רשימת-נמענים-דינמית-4a91aa9b.md)

## Custom fields (יצירה ועריכה של שדות מותאמים)
Per-list extra fields (e.g. city, plan, birthday) used for personalization & targeting.
- Article: [offline article catalog](articles/INDEX.md)

## Manage / edit / settings
- Manage list: [offline article](articles/ניהול-רשימת-נמענים-7f7e662f.md)
- Edit settings: [offline article](articles/עריכת-הגדרות-של-רשימה-baa03056.md)
- List tags: [offline article](articles/הוספת-תגיות-לרשימה-f58477e1.md)
- "All recipients" list: [offline article](articles/רשימת-כל-הנמענים-ואיך-עובדים-איתה-6b67ff1a.md)
- List statistics: [offline article](articles/INDEX.md)
- Double opt-in: [offline article](articles/אישור-כפול-double-opt-in-8a688459.md)

---

## Recipients (נמענים)

### Add one manually (הוספת נמען לרשימה)
- Article: [offline article](articles/איך-מוסיפים-ידנית-נמען-לרשימה-b3307406.md)

### Import from a file (ייבוא רשימת נמענים מקובץ חיצוני)
**Files:** CSV or TXT only; one record per line; fields separated by comma or tab.
1. From the recipients screen pick the target list → **"ייבוא" (Import)** (or list
   settings → Import). You can add several lists to update at once.
2. **Load recipients:** upload the file (state comma/tab separator) **or** paste data
   manually. Click Next.
3. **Field mapping** (critical): map each column to a system/custom field. You must
   map at least **Email or Phone**.
   - **"שם מלא" (Full name):** auto-splits on first space into first/last.
   - **Dates:** use `YYYY-MM-DD`, `YYYY/MM/DD`, `DD-MM-YYYY`, or `DD/MM/YYYY` — avoid US
     month-first format.
   - **Phone:** digits only, one optional hyphen ("052-1234567").
   - Tick "ignore first row" if it's a header. Tags column = separated by semicolons.
4. **Import settings:** if a recipient already exists, choose update-or-keep and whether
   to refresh their join date; name the import (appears in history); optionally tag all
   imported; accept terms; click **"סיום" (Complete)**.
5. Runs in the background — you're notified when done.

**Status fields during import** (value 1 = apply the negative status, 0 = stay active):
- "Inactive in system", "Doesn't receive SMS", "Unwanted email" (blacklist),
  "Inactive in list". Marking system-inactive on import is **irreversible** via import.
- Article: [offline article](articles/ייבוא-נמענים-מקובץ-חיצוני-2f802723.md)
- Import tags: [offline article](articles/INDEX.md)

### Export a list to a file (ייצוא רשימת נמענים לקובץ)
- Article: [offline article](articles/ייצוא-רשימת-נמענים-לקובץ-5e006703.md)

### Move / copy recipients between lists (העברה והעתקה)
- Article: [offline article](articles/העברה-והעתקה-של-נמענים-בין-רשימות-57172023.md)

### Other recipient tasks
- Update details: [offline article](articles/איך-מעדכנים-פרטי-נמען-b97c733c.md)
- Search: [offline article](articles/חיפוש-נמענים-e131c96d.md)
- Tags on a recipient: [offline article](articles/הוספת-תגיות-לנמען-bbcd0193.md)
- Re-adding to a list: [offline article](articles/מה-קורה-כשנמען-מתווסף-שוב-לרשימה-389785e1.md)
- Subscribe/unsubscribe notifications: [offline article](articles/הודעה-על-הצטרפות-עזיבה-של-נמענים-466c9a11.md)

### Recipient statuses (סטטוסים)
- Overview: [offline article](articles/סטטוסים-של-נמענים-ברשימות-דיוור-dc36cd59.md)
- Inactive account-wide: [offline article](articles/נמען-בסטטוס-לא-פעיל-ברמת-החשבון-9790e903.md)
- Active/inactive in a specific list: [offline article](articles/סטטוס-פעיל-לא-פעיל-ברשימה-ספציפית-da1a8532.md)
- SMS inactive: [offline article](articles/סטטוס-נמען-לא-פעיל-sms-2c2e3842.md)
- Star rating: [offline article](articles/דירוג-כוכבים-של-נמען-מהו-ולמה-הוא-משמש-9ad695b2.md)
