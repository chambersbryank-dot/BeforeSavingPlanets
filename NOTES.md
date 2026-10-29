- Oct 28 (overnight) v4 hero smoothing: Sun→planet crossfade (sun 0.1–5.7s eased in/out, planet 1.6–6.4s ease-out); Theia eases in 3.7s and fades into impact at ~5.5s (no longer lingers); flash softened (peak .82, warm white, 2.6s decay); shockwave now soft glow ring instead of hard disk; debris fades in/out on eased curve; Moon drifts 6.4s; kicker WHERE IT ALL BEGINS 7s (2s ease), title 9s (+2s), CTAs 10.6s. Hero images preloaded (sun + stars high priority) on all 6 home pages via scripts/build.py. Reduced-motion unchanged.
- Oct 28 v3 hero: "WHERE IT ALL BEGINS" larger (clamp 1.25–2.4rem), absolutely centered between nav bottom and planet top; kicker fades in at 5.4s, title at 7.4s (+2s), CTAs 8.6s.

## 2026-10-28 — Hero v2: cinematic photoreal Earth formation
- Replaced SVG hero with SI-made photoreal layers in assets/hero/ (stars-nebula, sun, molten-earth, theia WebP, all <220KB). Artist's interpretation — Made from SI and Biological SI Partner; science NASA/USGS.
- Timeline: big Sun blazes then fades (0–4.3s) as molten cracked Earth forms (1.8–6.4s); Theia streaks in, impact flash + shockwave + debris (5.2s); planet cools, Moon drifts out; title 6s, small WHERE IT ALL BEGINS above title (centered between nav and title) 6.6s.
- Scene markup: scripts/hero.html (build.py). Reduced motion = static end frame.

# NOTES (newest first)

## 2026-10-28 — Earth-formation hero + Dig Quest prototype
- Home hero: new 7s SVG/CSS animation (`scripts/hero.svg`, `bsp.css`): cloud → Sun+disk → accretion → planet grows → Theia impact + debris ring → Moon → magma ocean cools to blue Earth → title rises; "WHERE IT ALL BEGINS" (all 6 langs) fades in huge behind the H1 at 5.6–7.2s. Pause button kept; prefers-reduced-motion shows final frame. Labeled "artist’s interpretation … not real footage".
- Science brief + storyboard + PD media upgrade options: `/workspace/beforesavingplanets/earth-formation-hero-brief.md` (box path).
- New `Quest.html` (x6 langs): 8 cited layers (4.54 Ga → LGM 20 ka), progress counter (`bsp-quest.js`), image placeholders naming the PD source to fetch, bridge cards to savingplanets.com Oceans / Deforestation / Coral_Restoration_Foundation / Polar. English copy in all langs, marked TODO machine-draft.
- Home: "Start the Dig Quest" CTA + teaser card; footer link.
- Needs Bryan: pick real PD images per layer; approve hero art; translations.
