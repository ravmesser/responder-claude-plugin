# Automations (אוטומציות)

An automation is a **branching flow** that runs per-recipient: a trigger starts it,
then actions/conditions/delays move the recipient through a path. Use it when behaviour
should change the path (vs. a fixed series, or a rule-based dynamic list).

## List vs dynamic list vs automation (decision note)
- **Static list:** manual membership. (`lists-and-recipients.md`)
- **Dynamic list:** auto membership from rules — good for **segmentation** ("everyone
  tagged VIP"). No steps/timing.
- **Series:** fixed sequence of emails per recipient. (`email-series.md`)
- **Automation:** multi-step flow with **conditions and branching** — good when the next
  action depends on what the recipient did (opened, clicked, bought).
- Dynamic-list-vs-automation: [offline article catalog](articles/INDEX.md)

## Element types in an automation (סוגי האלמנטים באוטומציה)
- **Trigger (טריגר):** the condition that starts the flow (e.g. joined a list, tag added).
- **Action (פעולה):** the core operations — add to list, send email, update tags, etc.
- **Delay (השהיה):** wait a duration (minutes/hours/days) or until an event (e.g. opened).
- **Split (פיצול):** create two parallel branches that both run on the same recipient.
- **Condition (תנאי):** branch by whether a criterion is met — separate true/false paths.
- **End (סיום):** terminates a branch. **Every branch must end** with this element.
- Article: [offline article](articles/סוגי-האלמנטים-באוטומציה-ed161f16.md)

## Create / edit an automation (יצירה או עריכה)
General flow: open Automations → new automation → place a **Trigger**, then chain
**Actions / Delays / Conditions / Splits**, and close each branch with **End**. Keep it
inactive while building, then activate.
- Article (creating/editing): [offline article catalog](articles/INDEX.md)
- Common examples: [offline article catalog](articles/INDEX.md)

## Related
- Automatic list cleaning (ניקיון רשימות אוטומטי): [offline article catalog](articles/INDEX.md)
- Star rating (דירוג כוכבים): [offline article catalog](articles/INDEX.md)
- Impact of changes on a live series: [offline article catalog](articles/INDEX.md)
- Webhook trigger: [offline article](articles/INDEX.md)
- Cardcom payment trigger: [offline article catalog](articles/INDEX.md) (see `integrations.md`)
