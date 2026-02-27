# Willkommen bei ComplianceOS

**ComplianceOS** ist eine KI-gestützte On-Premise-Plattform für automatisierte Compliance-Audits gegen 9 internationale Sicherheitsstandards. Die Anwendung läuft vollständig auf Ihrer eigenen Infrastruktur — keine Daten verlassen Ihr Netzwerk.

<figure class="screenshot" markdown>
![ComplianceOS Dashboard](screenshots/dashboard/dashboard-overview.png)
<figcaption>Dashboard mit Compliance-Score, Domain-Übersicht und Findings-Heatmap</figcaption>
</figure>

---

## Was ist ComplianceOS?

ComplianceOS prüft Ihre IT-Infrastruktur automatisiert gegen anerkannte Sicherheitsstandards. Die Plattform kombiniert regelbasierte Checks mit KI-gestützter Analyse und liefert konkrete, nachvollziehbare Handlungsempfehlungen.

**Für wen ist ComplianceOS gedacht?**

- **Compliance-Beauftragte**, die ihre Audit-Zyklen beschleunigen wollen
- **CISOs**, die einen aktuellen Überblick über den Sicherheitsstatus benötigen
- **Geschäftsführung**, die Compliance-Risiken in Geschäftskennzahlen verstehen will
- **IT-Teams**, die konkrete technische Massnahmen priorisieren müssen

!!! info "Drei Ansichten für drei Rollen"
    ComplianceOS bietet dedizierte Dashboard-Ansichten für **Compliance**, **CISO** und **Management** — jede Rolle sieht genau die Informationen, die sie braucht.

---

## Kernfunktionen

<div class="feature-grid" markdown>

<div class="feature-card" markdown>
### 9 Standards
ISO 27001, ISO 22301, ISO 27005, ISO 27017, ISO 27018, ISO 27035, NIS2, BSI IT-Grundschutz, DSGVO
</div>

<div class="feature-card" markdown>
### 135 Controls
Technische Prüfpunkte mit automatisierten Checks über 12 Sicherheitsdomänen
</div>

<div class="feature-card" markdown>
### KI-Chat
Compliance-Beratung per integriertem Chat mit Claude AI (optional)
</div>

<div class="feature-card" markdown>
### Audit-Engine
Vollständige oder domainspezifische Audits mit Live-Fortschrittsanzeige
</div>

<div class="feature-card" markdown>
### Policy-Generator
6 Vorlagen für Richtlinien — automatisch generiert mit Standard-Referenzen
</div>

<div class="feature-card" markdown>
### Drift-Detection
Vergleich aufeinanderfolgender Audit-Läufe zur Erkennung von Regressionen
</div>

<div class="feature-card" markdown>
### Risiko-Dashboard
5x5-Risikomatrix, geschätzter finanzieller Impact, Compliance-Trends
</div>

<div class="feature-card" markdown>
### Cross-Standard-Mapping
Netzwerk-Visualisierung der Überschneidungen zwischen allen 9 Standards
</div>

</div>

---

## Schnellstart

=== "Docker (empfohlen)"

    ```bash
    git clone https://github.com/silentspike/complianceos.git
    cd complianceos
    docker compose up -d
    ```

    Dann öffnen Sie [http://localhost:8001](http://localhost:8001) im Browser.

=== "pip"

    ```bash
    git clone https://github.com/silentspike/complianceos.git
    cd complianceos
    python -m venv .venv && source .venv/bin/activate
    pip install -e ".[ai,docs]"
    make dev
    ```

!!! tip "Erster Schritt nach dem Start"
    Nach dem Start werden Sie auf die **Setup-Seite** weitergeleitet, um Claude AI zu verbinden. Danach legen Sie ein Projekt an und führen Ihren ersten Audit durch. Folgen Sie der Anleitung unter [Erste Schritte](schnellstart/erste-schritte.md).

---

## Mit und ohne Claude AI

ComplianceOS ist als **eigenständige Plattform** konzipiert. Claude AI ist eine optionale Erweiterung — alle Kernfunktionen laufen vollständig lokal.

=== "Ohne Claude AI"

    | Funktion | Verfügbarkeit |
    |----------|--------------|
    | Audit-Engine (135 Controls, 12 Domains) | Vollständig verfügbar |
    | Automatisierte Checks (71 Controls) | Volle Genauigkeit (regelbasiert, deterministisch) |
    | Findings-Browser mit Filter und Export | Vollständig verfügbar |
    | Remediation-Tracking (Kanban-Board) | Vollständig verfügbar |
    | Alle Reports (Audit, Drift, Cross-Standard, Matrix) | Vollständig verfügbar |
    | Dashboard (Score-Ring, Heatmap, Domain-Scores) | Vollständig verfügbar |
    | Executive Dashboard (Risiko-Matrix, KPI) | Vollständig verfügbar |
    | Dokumente (Upload, Parser-Pipeline) | Vollständig verfügbar |
    | Policy-Generierung | Basisversion (statische Templates) |
    | Chat | Builtin-Responses zu häufigen Fragen |

=== "Mit Claude AI (empfohlen)"

    Zusätzlich zu allen Basisfunktionen:

    | Funktion | Verbesserung |
    |----------|-------------|
    | KI-gestützte Audit-Bewertung | Semantische Analyse der Evidenz, höhere Confidence |
    | Manuelle Checks (53 Controls) | KI analysiert Dokumente inhaltlich statt nur per Pattern |
    | Policy-Generierung | Kontextbezogene Richtlinien basierend auf Ihren Findings |
    | Chat | Interaktive Compliance-Beratung mit 9 Intent-Typen |
    | Hybrid Checks (11 Controls) | KI ergänzt automatische Checks mit organisatorischer Bewertung |

!!! info "KI-Setup überspringen"
    Wenn Sie ComplianceOS ohne Claude AI nutzen möchten, überspringen Sie die Setup-Seite beim ersten Start. Alle Kernfunktionen stehen sofort zur Verfügung. Sie können Claude AI jederzeit später unter [Einstellungen](bedienung/einstellungen.md) verbinden.

Für eine detaillierte technische Erklärung der Audit-Engine und Bewertungsmethoden siehe [Audits > Wie funktioniert die Audit-Engine?](bedienung/audits.md#wie-funktioniert-die-audit-engine).

---

## Seitenübersicht

### Start

| Seite | Beschreibung |
|-------|-------------|
| [Installation](schnellstart/installation.md) | Voraussetzungen, pip- und Docker-Installation |
| [Claude-Setup](schnellstart/setup.md) | OAuth-Authentifizierung mit Claude AI |
| [Erste Schritte](schnellstart/erste-schritte.md) | Projekt anlegen, ersten Audit durchführen |
| [Docker](schnellstart/docker.md) | Docker Compose Konfiguration und Betrieb |
| [Datenschutz](schnellstart/datenschutz.md) | Welche Daten wohin fliessen, lokale Verarbeitung |

### Bedienung

| Seite | Beschreibung |
|-------|-------------|
| [Dashboard](bedienung/dashboard.md) | Compliance-Score, Domain-Übersicht, Findings-Heatmap |
| [Audits](bedienung/audits.md) | Audit starten, Fortschritt, Ergebnisse, Vergleich |
| [Findings](bedienung/findings.md) | Findings filtern, Severity, Status-Workflow |
| [Remediation](bedienung/remediation.md) | Kanban-Board, Listen-Ansicht, Burndown-Chart |
| [Chat](bedienung/chat.md) | KI-gestützte Compliance-Beratung, 9 Intent-Typen |
| [Dokumente](bedienung/dokumente.md) | Upload, Parser-Pipeline, Analyse |
| [Policies](bedienung/policies.md) | 6 Vorlagen, Generierung, Registry |
| [Reports](bedienung/reports.md) | Audit-Report, Drift-Detection, PDF-Export |
| [Executive](bedienung/executive.md) | Risiko-Matrix, Business Impact, KPI-Trends |
| [Einstellungen](bedienung/einstellungen.md) | Präferenzen, Projekte, Schedules, ntfy |

### Referenz

| Seite | Beschreibung |
|-------|-------------|
| [Standards](referenz/standards.md) | Alle 9 unterstützten Standards im Detail |
| [Glossar](referenz/glossar.md) | Fachbegriffe von A bis Z |
| [Tastaturkürzel](referenz/tastaturkuerzel.md) | Keyboard-Shortcuts und Command-Palette |
| [FAQ](referenz/faq.md) | Häufig gestellte Fragen |

---

## Technische Eckdaten

| Eigenschaft | Wert |
|-------------|------|
| **Stack** | FastAPI + HTMX + Jinja2 + SQLite |
| **KI-Integration** | Claude AI (optional, per OAuth) |
| **Standards** | 9 (ISO 27001, 22301, 27005, 27017, 27018, 27035, NIS2, BSI, DSGVO) |
| **Controls** | 135 technische Prüfpunkte |
| **Domains** | 12 Sicherheitsbereiche |
| **AUDIT-CHECKs** | 2.042 semantische Anforderungen |
| **Deployment** | Docker Compose oder pip install |
| **Datenbank** | SQLite (WAL-Modus, lokal) |
| **Lizenz** | Apache-2.0 |

!!! warning "Rechtlicher Hinweis"
    ComplianceOS ist ein technisches Werkzeug zur Unterstützung von Compliance-Audits. Es ersetzt keine professionelle Rechts- oder Compliance-Beratung. Die Ergebnisse der automatisierten Prüfungen müssen von qualifiziertem Fachpersonal verifiziert werden.
