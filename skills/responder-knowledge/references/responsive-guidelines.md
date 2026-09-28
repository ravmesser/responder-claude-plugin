# Responsive Landing Pages — Technical Reference

Why fluid landing pages overflow, and how to stop it. Focused on the one trap
that isn't obvious; the mechanism is included so the rule stays correct in cases
not listed here.

## The grid/flex minimum-size trap

**Symptom:** desktop looks fine; on a narrow viewport something refuses to shrink,
overflows its column, and causes horizontal scroll. Collapsing the grid to one
column in a media query does *not* fix it.

**Mechanism:** grid and flex items default to `min-width: auto`, which resolves to
the item's **min-content size** — not zero. So an item containing a wide image,
an unbreakable string, an iframe, or an embedded widget with an intrinsic width
inherits that width as a hard floor and won't shrink below it. The track narrows;
the item doesn't; it overflows.

**Fix:**

```
.grid-item {
  min-width: 0;      /* removes the min-content floor so the item can shrink */
  max-width: 100%;   /* never exceed the track */
}
```

`overflow: hidden` (or `auto`/`scroll`) *also* drops the floor to zero — the
automatic minimum only applies while `overflow` is `visible`. That's why
`overflow: hidden` on a wrapper can make an embedded widget suddenly go
responsive: it isn't just clipping, it's unlocking the shrink so a fluid child
can reflow. Use `min-width: 0` when you don't want clipping.

**Only applies to grid/flex items.** A plain `display: block` container has no
automatic minimum, so the same widget behaves fine there. This is why one form is
responsive in a block and broken in a grid cell on the same page — the difference
is the container's `display`, not the form.

**Rule:** any grid/flex item holding an image, iframe, embed, or third-party
widget gets `min-width: 0; max-width: 100%` up front.

## Embedded third-party form scripts

A form injected by an external script (e.g. `<script src="//form2.ravpage.co.il/...">`)
doesn't exist when you write your CSS — it's injected at load, so you're styling
blind. Assume it has an intrinsic width.

- Inline HTML embed → container rules above reach it.
- Iframe embed → your CSS can't touch its internals; only constrain the iframe box
from outside (`width: 100%; max-width: 100%`). Its content is responsive only if
the provider made it so.
- If the tool that *creates* the form exposes a width (e.g. `form_width`, often
defaulting to ~400px), set it to fit your narrowest target instead of leaving
the default. Prevention beats containment.

The most robust fix is upstream — the widget setting `max-width: 100%` in its own
CSS so it self-defends in any container. You can't do that from the page side;
the container rules are a workaround, not the root fix.

## Baseline

- `<meta name="viewport" content="width=device-width, initial-scale=1">` — without
it, mobile renders at a fake ~980px and no media query behaves.
- `img, video, iframe { max-width: 100%; height: auto; }`
- Long unbreakable strings: `overflow-wrap: anywhere` on text containers.
- Prefer `max-width` + `width: 100%` over bare fixed `width:` in the content flow.
- Account for padding: a 400px child + 28px padding each side needs ~456px to fit.
- `html, body { overflow-x: hidden }` masks overflow — a diagnostic, not a fix.

## Why media queries aren't enough

Media queries restructure layout (columns, stacking, scale). They don't shrink a
child that can't shrink — that's an intrinsic-size problem, not a layout one. A
page can pass the "does it stack on mobile?" glance and still overflow. Test at
the narrowest width (~320px), not just at your breakpoints.

## Checklist

1. Viewport meta tag present.
2. Drag from full width to ~320px — watch for horizontal scroll.
3. Every grid/flex item with an image/embed/long string has `min-width: 0`
(or `overflow: hidden`) and `max-width: 100%`.
4. Every `img`/`iframe`/`video` capped at `max-width: 100%`.
5. Third-party widgets created at a sensible width and wrapped safely.
6. No bare fixed `width:` in the main content flow.
