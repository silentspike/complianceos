# OpenGraph Social-Preview Spec

> **Hinweis:** Diese Datei beschreibt die Spec fuer das Custom-Social-Preview-Bild
> des Repositories. Das Bild selbst muss durch den Repo-Maintainer in
> Repository Settings → Social Preview hochgeladen werden — die GitHub-API
> bietet dafuer keinen automatisierten Weg.

## Format-Anforderungen

| Eigenschaft | Wert |
|---|---|
| Aufloesung | 1280 × 640 px (GitHub Empfehlung) |
| Dateiformat | PNG (bevorzugt) oder JPG |
| Maximalgroesse | < 1 MB |
| Farbraum | sRGB |
| Tone | nuechtern, customer-tauglich (kein bunter Marketing-Stil) |

## Layout

Drei-Spalten-Layout, von links nach rechts:

### Linke Spalte (35 % Breite) — Brand

- ComplianceOS-Wortmarke (Schrift Outfit, Bold, weiss auf Dark-Theme-Hintergrund)
- Tagline darunter: "KI-gestuetzte On-Premise Compliance-Audit-Plattform"
- Kleines Versions-Tag rechts unten: "v1.0.2"

### Mittlere Spalte (40 % Breite) — Standards

3×3 Grid mit den 9 Compliance-Standards-Logos (oder Text-Badges):
- ISO/IEC 27001
- ISO 22301
- ISO/IEC 27005
- ISO/IEC 27017
- ISO/IEC 27018
- ISO/IEC 27035
- NIS2
- BSI IT-Grundschutz
- DSGVO

### Rechte Spalte (25 % Breite) — Trust-Signal

- On-Prem-Symbol (Server/Building-Icon)
- "Optional AI" als Klammer-Hinweis (kein Tool-Logo prominent — nur generisches AI-Icon)
- "EULA · 90-Day Pilot" als Zeile

## Farbpalette (Obsidian Prism Design System)

- Hintergrund: Sapphire-Tiefe `#0F1419` oder `#1A1F2C`
- Primaer-Akzent: Sapphire `#3B82F6`
- Sekundaer-Akzent: Amethyst `#A855F7`
- Erfolgs-Indikator: Emerald `#10B981`
- Schrift: weiss `#F5F5F5` oder gebrochenes Weiss `#E5E5E5`

## Tools fuer die Erstellung

1. **Inkscape** (SVG) → PNG-Export bei 1280×640. SVG-Quelldatei ablegen unter `docs/assets/opengraph-source.svg` fuer spaetere Anpassungen.
2. **Figma** als Alternative — Frame 1280×640, Export als PNG @ 2x → 2560×1280, dann auf 1280×640 down-skalieren fuer scharfe Kanten.
3. **CLI-Alternative** mit `pillow` oder ImageMagick fuer reproduzierbare Builds (nice-to-have, nicht Pflicht).

## Cross-Cutting

- Tool-agnostisch: kein Codex-/Claude-/Anthropic-Logo prominent. "Optional AI" bleibt generisch.
- Keine OpenGraph-Spezifik die nur fuer eine Reviewer-Gruppe (z.B. OpenAI) Sinn ergibt — das Bild wird von allen Repo-Visitors gesehen.

## Action fuer Repo-Maintainer

1. Bild gemaess obiger Spec erstellen
2. SVG-Quelldatei in `docs/assets/opengraph-source.svg` committen
3. PNG-Export hochladen via GitHub-Repo Settings → Social Preview → Upload
4. Mit `curl -sI https://opengraph.githubassets.com/0/silentspike/complianceos` verifizieren dass Custom-Image ausgeliefert wird (statt Default-Repo-Banner)

## Verweise

- [Architektur-Ueberblick](../architecture.md)
- [GitHub Docs: Customizing your repository's social media preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
