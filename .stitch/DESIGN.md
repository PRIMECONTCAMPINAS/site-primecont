# Design System: PRIMECONT Website
**Project ID:** 4721706287526653716

## 1. Visual Theme & Atmosphere
A restrained, corporate-elegant, and gallery-airy interface with stable but confident asymmetric layouts, and fluid spring-physics motion. The atmosphere is clinical yet warm — like a well-lit premium architecture studio. It conveys absolute structure, calm, and sophistication.

## 2. Color Palette & Roles
- **Canvas White** (#FFFFFF) — Primary background surface.
- **Pure Surface** (#F9FAFB) — Secondary backgrounds and subtle section contrasts.
- **Deep Navy Black** (#0B2430) — Primary text, deep headers, and highly contrasted institutional blocks.
- **Prime Blue** (#10465E) — The single accent color (Saturation <80%). Used for primary buttons, focus rings, and active states.
- **Muted Steel Blue** (#3D707D) — Secondary text, metadata, supporting details and icons.
- **Whisper Border** (rgba(61, 112, 125, 0.15)) — Card borders, 1px structural dividing lines.

## 3. Typography Rules
- **Display:** Outfit — Track-tight, controlled scale, weight-driven hierarchy. Used for confident, authoritative headlines.
- **Body:** Geist — Relaxed leading, 65ch max-width, neutral secondary color. Highly readable and modern.
- **Mono:** Geist Mono — For code, metadata, highly structured numbers.
- **Banned:** Inter, generic system fonts (Times New Roman, Georgia).

## 4. Component Stylings
- **Buttons:** Flat, extremely elegant, no outer glow. Tactile -1px translate on active state. Prime Blue (#10465E) fill for primary, ghost/outline with whisper borders for secondary.
- **Cards:** Sophisticated, subtly rounded corners (0.5rem - 0.75rem). Diffused whisper-soft shadow. Used only when elevation serves hierarchy. For high-density areas, replace with border-top dividers or negative space.
- **Inputs:** Label above, error below. Focus ring in Prime Blue. Minimalist and clear.
- **Loaders:** Skeletal shimmer matching exact layout dimensions. No circular spinners.
- **Empty States:** Composed, illustrated compositions — not just "No data".

## 5. Layout Principles
Grid-first responsive architecture. Generous asymmetric splits for Hero sections (referencing Clifford Chance & Northlane rhythm).
Strict single-column collapse below 768px. Max-width containment (e.g., 1200px - 1400px).
No flexbox percentage math. Generous internal padding and heavy reliance on whitespace.
No overlapping elements — clean spatial separation always.

## 6. Motion & Interaction
Spring physics for all interactive elements (stiffness: 100, damping: 20).
Staggered cascade reveals for loading. Perpetual micro-loops on active dashboard components.
Hardware-accelerated transforms only (opacity and transform).

## 7. Anti-Patterns (Banned)
- NO emojis anywhere.
- NO Inter font, NO pure black (#000000).
- NO neon glows, NO outer drop shadows that look dirty.
- NO 3-column equal card layouts (use zig-zag, horizontal scroll or asymmetric cards).
- NO AI copywriting clichés ("Elevate", "Seamless", "Unleash").
- NO generic placeholder names ("Acme", "John Doe").
- NO filler UI text ("Scroll to explore", "Swipe down", bouncing chevrons).
- NO photos of handshakes, calculators, generic stock corporate people.
- NO overlapping of text over busy image backgrounds (always clear zones).
