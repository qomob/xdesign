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

## Three Dials (internal configuration variables)

Once a direction is chosen (or during generation), set three internal variables that govern layout, motion, and density decisions. **These are invisible to the user** — they are configuration for the agent, recorded in the HTML reasoning block.

| Dial | Range | 1 = | 10 = | Baseline |
|------|-------|-----|------|----------|
| `DESIGN_VARIANCE` | 1-10 | Perfect symmetry, centered layouts | Asymmetric, experimental, bento grids | 7 |
| `MOTION_INTENSITY` | 1-10 | Static, hover-only | Cinematic, scroll-driven, physics | 5 |
| `VISUAL_DENSITY` | 1-10 | Art gallery, generous whitespace | Dense dashboard, packed data | 4 |

### Dial inference from user signals

| User signal | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| "简约 / clean / calm / editorial / Linear 风格" | 4-5 | 3-4 | 2-3 |
| "高端消费 / Apple 风格 / luxury / brand" | 6-7 | 5-6 | 3-4 |
| "活泼 / wild / Dribbble / Awwwards / experimental / agency" | 8-9 | 7-9 | 3-4 |
| "落地页 / portfolio / marketing site（默认）" | 6-8 | 5-7 | 3-5 |
| "trust-first / public-sector / regulated / accessibility" | 3-4 | 2-3 | 4-5 |
| "dashboard / 数据看板 / admin" | 5-6 | 3-4 | 7-8 |

### How dials drive output

- **VARIANCE ≥ 7** → use asymmetric layouts, bento grids, mixed cell sizes, deliberate imbalance
- **VARIANCE ≤ 5** → use centered or standard grid layouts, predictable hierarchy
- **MOTION ≥ 6** → add scroll-triggered reveals, parallax, magnetic hover; use Mode 3 animation primitives
- **MOTION ≤ 4** → hover states only, no scroll animation; respect `prefers-reduced-motion` by default
- **DENSITY ≥ 6** → compact spacing, multi-column data, smaller type scale, information-rich components
- **DENSITY ≤ 4** → generous spacing, large type, one idea per viewport, breathing room

### Recording in HTML reasoning block

```html
<!--
DESIGN REASONING
Dials: VARIANCE=7, MOTION=5, DENSITY=4
Direction: Balanced (B)
Theme seed: tokyo-night + Vercel tokens
-->
```

---

## Execution flow (5 phases)

### Phase 1 — Brief Inference (read the room, don't interrogate)

Before asking questions, **infer from available signals**. Most of the time the user has already given enough context — you just need to read it.

**6 signal dimensions to scan:**

| Signal | What to look for | If present |
|---|---|---|
| **1. Page kind** | Landing page / portfolio / dashboard / deck / animation / redesign | Determines mode routing and template selection |
| **2. Vibe words** | "简约", "高端", "科技感", "活泼", "editorial", "brutalist", "Linear 风格" | Sets the Three Dials directly (see inference table above) |
| **3. Reference signals** | Brand name, URL, screenshot, competitor mentioned | Triggers DESIGN.md fast path or Brand Asset Protocol |
| **4. Audience** | B2B buyers / consumers / developers / recruiters / investors / students | The audience picks the aesthetic, not the designer's taste |
| **5. Existing brand assets** | Logo, color, type, photography already available | These are starting material, not optional input |
| **6. Quiet constraints** | Accessibility-first, public-sector, regulated industry, kids' product, trust-first commerce | These constraints **override** aesthetic preference |

**Output a one-line "Design Read" before generating:**

State in one line: *"Reading this as: [page kind] for [audience], with a [vibe] language, leaning toward [design system or aesthetic family]."*

Examples:
- *"Reading this as: B2B SaaS landing for technical buyers, with a Linear-style minimalist language, leaning toward corporate-clean theme + restrained motion."*
- *"Reading this as: solo designer portfolio for hiring managers, with an editorial language, leaning toward japanese-minimal theme + scroll-driven animation."*

**When to ask:** Only when the design read genuinely diverges — you cannot confidently infer the direction. Ask **exactly one** question, not a multi-question dump. Example: *"Should this feel closer to Linear-clean or Awwwards-experimental?"*

**When NOT to ask:** If you can confidently infer from context, declare the design read and proceed. Asking unnecessary questions wastes the user's time and signals incompetence.

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
