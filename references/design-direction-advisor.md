# Design Direction Advisor (Fallback Mode)

> **Extracted from main SKILL.md** to keep the entry file under 500 lines.
> Load this file when Mode 2/3 receives a vague request with no brand or style reference.

---

## Why this exists

When the user says "帮我做个好看的页面" or "设计一个 dashboard" without naming a brand, giving a screenshot, or pointing at a reference URL, the default behavior is to produce a generic "universal design" — the statistical average of everything in the training data. That average carries zero brand signal. The result looks like it could belong to any company, which means it belongs to no one.

The Direction Advisor interrupts that default. Instead of guessing once and hoping, it surfaces **three differentiated directions** as real visual mockups, lets the user pick, then enters the normal PPAF loop with a confirmed direction.

**Core principle:** Never make the user blind-select a style from text descriptions. Show real visuals, then let them choose.

---

## When to trigger

**Trigger (any one):**
- Request is visually vague: "做个好看的", "帮我设计", "design something nice", no style keyword
- User explicitly asks for direction: "推荐几个风格", "给几个方向", "not sure what style"
- No brand name, no screenshot, no reference URL, no Figma export in the input
- User says "我也不知道要什么风格"

**Skip (any one):**
- User named a brand → use the [DESIGN.md fast path](./design-system-catalog.md)
- User gave a screenshot / Figma / reference URL → extract tokens, go straight to PPAF
- User specified a concrete style: "Apple Silicon 风格发布会" → straight to Junior Designer flow
- Small edit or tool call: "把这个转成 PDF" → no direction needed

**Ambiguous?** Use the lightweight version: list 3 differentiated directions with one-line descriptions, ask the user to pick. Do not generate full mockups until the user engages.

---

## The three-direction method

Generate three directions that span a spectrum from **safe/conventional** to **distinct/novel**. Each direction must be visually distinct from the other two — not three variations of the same idea.

### Direction A — Information-first (by-the-book)

The safe, professional baseline. Content density, data clarity, conventional layout patterns. This is what a competent designer would produce on autopilot.

- **Visual tone:** clean, structured, neutral
- **Layout:** standard grid, predictable hierarchy
- **Color:** restrained — one accent color on neutral background
- **Use when:** the user's audience expects professionalism over surprise (enterprise, fintech, B2B)

### Direction B — Conversion/experience-first (balanced)

Adds personality while staying functional. Stronger visual hierarchy, deliberate accent moments, considered typography.

- **Visual tone:** confident, warm or cool depending on content, branded but not loud
- **Layout:** intentional asymmetry or deliberate focal points
- **Color:** 2-color system with intentional contrast
- **Use when:** the user wants to stand out without scaring anyone (SaaS, product launch, marketing site)

### Direction C — Concept-led (novel)

The bold option. A distinct visual philosophy — editorial, brutalist, cinematic, or experimental — that commits to a point of view.

- **Visual tone:** strong personality, may divide opinion
- **Layout:** unconventional grid, dramatic scale contrast, full-bleed moments
- **Color:** opinionated palette (monochrome, high-contrast, or unexpected accent)
- **Use when:** the user wants a signature look, the brand is new and needs to differentiate, or the audience is design-literate

---

## Ammunition library (use existing resources)

The three directions draw from XDesign's bundled assets — do not invent styles from scratch:

| Resource | Count | How to use |
|---|---|---|
| `deck-studio/assets/themes/` | 36 CSS themes | Each direction picks one theme as its visual seed |
| `assets/design-md/<brand>/DESIGN.md` | 58 brand systems | Map the user's industry to 2-3 relevant brands, extract token philosophy |
| `references/design-system-catalog.md` | Style categories | Use the "Style-to-Brand Mapping" table to find candidates |

**Mapping by industry:**

| User's domain | Direction A (safe) | Direction B (balanced) | Direction C (novel) |
|---|---|---|---|
| Developer tool / SaaS | `corporate-clean` + Linear tokens | `tokyo-night` + Vercel tokens | `neo-brutalism` + xAI tokens |
| Fintech / B2B | `swiss-grid` + Stripe tokens | `editorial-serif` + Wise tokens | `sharp-mono` + Coinbase tokens |
| Consumer / lifestyle | `soft-pastel` + Airbnb tokens | `sunset-warm` + Pinterest tokens | `magazine-bold` + Clay tokens |
| AI / ML platform | `minimal-white` + Claude tokens | `glassmorphism` + Cohere tokens | `cyberpunk-neon` + MiniMax tokens |
| Creative / portfolio | `japanese-minimal` + Figma tokens | `bauhaus` + RunwayML tokens | `memphis-pop` + Spotify tokens |
| Automotive / premium | `midcentury` + BMW tokens | `blueprint` + Tesla tokens | `vaporwave` + Lamborghini tokens |

When the user's domain doesn't match any row, default to: `corporate-clean` (A) → `editorial-serif` (B) → a theme from the "Colorful & Expressive" category (C).

---

## Execution flow (5 phases)

### Phase 1 — Clarify (one round, max 3 questions)

Ask in a single batch:
1. **Audience & context** — who sees this, what's the emotional goal
2. **Content scope** — what must appear (sections, data, features)
3. **Output format** — web page, deck, mobile, dashboard

Also ask for any reference the user can provide: a brand name, a URL, a screenshot, a competitor they like. If the user provides nothing, proceed to Phase 2.

### Phase 2 — Restate (≥100 words)

Paraphrase the core need back to the user. Show you understood the audience, the emotional register, and the unspoken expectations. End with: "I'll produce three differentiated visual directions for you to compare."

### Phase 3 — Generate three directions

For each direction, produce a **real visual mockup** (not a text description):
- Use `design_canvas.jsx` to show 2-3 options side-by-side, OR
- Produce three separate HTML files, each a single representative screen

Each mockup must include:
- A label: "Direction A — Information-first" etc.
- One sentence on the design philosophy
- The actual visual (layout, color, type, spacing)

**All three must share the same canvas size and content** — only the visual direction differs. Otherwise the comparison is meaningless.

### Phase 4 — User picks

Present the three directions. The user picks one, mixes elements from two, or rejects all three and gives new direction.

- If the user picks → enter normal PPAF loop (Phase 1: Design System First) with the chosen direction as the seed
- If the user mixes → note which elements from which direction, proceed
- If the user rejects → ask what specifically didn't work, regenerate with the feedback

### Phase 5 — Converge

Once a direction is confirmed, transition to the standard Mode 2/3 workflow. The chosen theme/tokens become the design system foundation. Do not re-litigate the direction — commit and execute.

---

## Anti-patterns

- ❌ **Text-only directions** — "Option 1: clean and minimal. Option 2: bold and colorful." The user cannot evaluate a style from adjectives. Always produce real visuals.
- ❌ **Three variations of the same thing** — if all three directions use a neutral background with one accent color, you haven't differentiated. Push Direction C to be genuinely unconventional.
- ❌ **Generating full deliverables before direction confirmation** — the three mockups are representative screens (one each), not the full 10-page deck or 6-screen app.
- ❌ **Ignoring user feedback in Phase 4** — if the user says "Direction B but warmer," that's the seed, not a suggestion to regenerate all three.
- ❌ **Skipping clarification entirely** — even in fallback mode, one round of questions prevents building the wrong thing.

---

## Relationship to other references

| Reference | Relationship |
|---|---|
| [mode-2-prototype.md](./mode-2-prototype.md) | Direction Advisor is a pre-phase to Mode 2's PPAF loop. After direction is confirmed, Mode 2 takes over. |
| [design-system-catalog.md](./design-system-catalog.md) | Provides the ammunition library (58 brands + style mapping). |
| [workflow-guide.md](./workflow-guide.md) | The PPAF loop that follows direction confirmation. |
| [brand-asset-protocol.md](./brand-asset-protocol.md) | If the user names a brand during Phase 1, exit the Advisor and run the asset protocol instead. |
