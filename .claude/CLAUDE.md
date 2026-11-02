# Working agreements for this portfolio (Nicolás Mogollón Barbosa)

These rules come from the site owner and apply to every task in this repo.

## Research before doing (mandatory)
- Before designing or building anything, research first. Use the newest sources available (current year), not memory.
- Cite what you found (links) when you report back, and say when a source could not be reached.
- Style can be our own and does not need to follow trends. Rules (UX, accessibility, SEO, i18n, performance, browser support) must follow the latest published guidance.

## Content and copy
- Do not change visible copy without approval. Propose text changes in a list, mark them in the HTML with `<!-- PROPUESTA DE TEXTO: ... -->`, and wait for a yes.
- The brand name is "Invest in Bogotá" (with tilde) everywhere.
- Talk to the owner in Spanish.

## Project context
- Brand/strategy context: `.agents/context/PRODUCT.md`.
- Current redesign work lives on the `redesign` branch under `redesign/`. The live site (`main`) is not touched without explicit approval.
- Backup of the original Framer export: branch `backup/original-framer-2026-11-01`.
- Visual concept "Horizonte": the logotype is letters rising from a line; its arcs, dot and stems are the shape vocabulary of the whole site.

## Delivery
- Verify every page visually (desktop + mobile) and with automated checks (axe, overflow, no-JS, reduced motion) before reporting.
- Do not crowd the site: every texture, animation or element needs a reason.

## Estado actual (para retomar en cualquier sesión)
- Trabajo vigente: Opción A v2 "Horizonte" en `redesign/a-v2/` (EN) y `redesign/a-v2/es/` (ES), rama `redesign`.
- Generador: las páginas se escriben a mano en HTML; CSS/JS compartidos en `redesign/a-v2/assets/` (`site.css`, `site.js`), enlazados con `?v=<hash>` para evitar cachés viejas. Si editas CSS/JS, actualiza el hash en todas las páginas.
- Decisiones tomadas por el dueño: textura = teselación (también como placeholder de imágenes); secciones oscuras aprobadas; panel de contacto con entrada desacelerada (sin morph); 404 con GIF aleatorio de gatos (GIPHY) dentro del sol; email `nicolasbarbosa.us@gmail.com`; título "Visual and AI Designer"; empresa "ReloQuest".
- Pendiente de aprobación: ver la sección "Pendiente de tu decisión" en `redesign/a-v2/PROPUESTAS.md` (ReloQuest, punto 9, puntos 11-14, versión en español, textos de interfaz, dominio).
- Nada se publica en `main` sin aprobación explícita.
- Deck de Figma del dueño (Figma Slides, fileKey `A2FLZyFCZUkYItYyTG2Tgn`, portada nodo `1:2107`): fondo negro tipo película, grano, polvo/rayas, quemadura de película naranja en una esquina y el logotipo con halación (núcleo amarillo, naranja, borde magenta). El conector de Figma solo puede capturar diapositivas cuyo enlace (node-id) comparta el dueño; no puede listar las diapositivas de un deck.
