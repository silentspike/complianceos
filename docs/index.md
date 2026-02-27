# Willkommen bei ComplianceOS

**ComplianceOS** ist eine KI-gestuetzte On-Premise-Plattform fuer automatisierte Compliance-Audits gegen 9 internationale Sicherheitsstandards. Die Anwendung laeuft vollstaendig auf Ihrer eigenen Infrastruktur — keine Daten verlassen Ihr Netzwerk.

<figure class="screenshot" markdown>
![ComplianceOS Dashboard](screenshots/dashboard/dashboard-overview.png)
<figcaption>Dashboard mit Compliance-Score, Domain-Uebersicht und Findings-Heatmap</figcaption>
</figure>

---

## Was ist ComplianceOS?

ComplianceOS prueft Ihre IT-Infrastruktur automatisiert gegen anerkannte Sicherheitsstandards. Die Plattform kombiniert regelbasierte Checks mit KI-gestuetzter Analyse und liefert konkrete, nachvollziehbare Handlungsempfehlungen.

**Fuer wen ist ComplianceOS gedacht?**

- **Compliance-Beauftragte**, die ihre Audit-Zyklen beschleunigen wollen
- **CISOs**, die einen aktuellen Ueberblick ueber den Sicherheitsstatus benoetigen
- **Geschaeftsfuehrung**, die Compliance-Risiken in Geschaeftskennzahlen verstehen will
- **IT-Teams**, die konkrete technische Massnahmen priorisieren muessen

!!! info "Drei Ansichten fuer drei Rollen"
    ComplianceOS bietet dedizierte Dashboard-Ansichten fuer **Compliance**, **CISO** und **Management** — jede Rolle sieht genau die Informationen, die sie braucht.

---

## Kernfunktionen

<div class="feature-grid" markdown>

<div class="feature-card" markdown>
### 9 Standards
ISO 27001, ISO 22301, ISO 27005, ISO 27017, ISO 27018, ISO 27035, NIS2, BSI IT-Grundschutz, DSGVO
</div>

<div class="feature-card" markdown>
### 135 Controls
Technische Pruefpunkte mit automatisierten Checks ueber 12 Sicherheitsdomaenen
</div>

<div class="feature-card" markdown>
### KI-Chat
Compliance-Beratung per integriertem Chat mit Claude AI (optional)
</div>

<div class="feature-card" markdown>
### Audit-Engine
Vollstaendige oder domainspezifische Audits mit Live-Fortschrittsanzeige
</div>

<div class="feature-card" markdown>
### Policy-Generator
6 Vorlagen fuer Richtlinien — automatisch generiert mit Standard-Referenzen
</div>

<div class="feature-card" markdown>
### Drift-Detection
Vergleich aufeinanderfolgender Audit-Laeufe zur Erkennung von Regressionen
</div>

<div class="feature-card" markdown>
### Risiko-Dashboard
5x5-Risikomatrix, geschaetzter finanzieller Impact, Compliance-Trends
</div>

<div class="feature-card" markdown>
### Cross-Standard-Mapping
Netzwerk-Visualisierung der Ueberschneidungen zwischen allen 9 Standards
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

    Dann oeffnen Sie [http://localhost:8001](http://localhost:8001) im Browser.

=== "pip"

    ```bash
    git clone https://github.com/silentspike/complianceos.git
    cd complianceos
    python -m venv .venv && source .venv/bin/activate
    pip install -e ".[ai,docs]"
    make dev
    ```

!!! tip "Erster Schritt nach dem Start"
    Nach dem Start werden Sie auf die **Setup-Seite** weitergeleitet, um Claude AI zu verbinden. Danach legen Sie ein Projekt an und fuehren Ihren ersten Audit durch. Folgen Sie der Anleitung unter [Erste Schritte](schnellstart/erste-schritte.md).

---

## Seitenuebersicht

### Start

| Seite | Beschreibung |
|-------|-------------|
| [Installation](schnellstart/installation.md) | Voraussetzungen, pip- und Docker-Installation |
| [Claude-Setup](schnellstart/setup.md) | OAuth-Authentifizierung mit Claude AI |
| [Erste Schritte](schnellstart/erste-schritte.md) | Projekt anlegen, ersten Audit durchfuehren |
| [Docker](schnellstart/docker.md) | Docker Compose Konfiguration und Betrieb |
| [Datenschutz](schnellstart/datenschutz.md) | Welche Daten wohin fliessen, lokale Verarbeitung |

### Bedienung

| Seite | Beschreibung |
|-------|-------------|
| [Dashboard](bedienung/dashboard.md) | Compliance-Score, Domain-Uebersicht, Findings-Heatmap |
| [Audits](bedienung/audits.md) | Audit starten, Fortschritt, Ergebnisse, Vergleich |
| [Findings](bedienung/findings.md) | Findings filtern, Severity, Status-Workflow |
| [Remediation](bedienung/remediation.md) | Kanban-Board, Listen-Ansicht, Burndown-Chart |
| [Chat](bedienung/chat.md) | KI-gestuetzte Compliance-Beratung, 9 Intent-Typen |
| [Dokumente](bedienung/dokumente.md) | Upload, Parser-Pipeline, Analyse |
| [Policies](bedienung/policies.md) | 6 Vorlagen, Generierung, Registry |
| [Reports](bedienung/reports.md) | Audit-Report, Drift-Detection, PDF-Export |
| [Executive](bedienung/executive.md) | Risiko-Matrix, Business Impact, KPI-Trends |
| [Einstellungen](bedienung/einstellungen.md) | Praeferenzen, Projekte, Schedules, ntfy |

### Referenz

| Seite | Beschreibung |
|-------|-------------|
| [Standards](referenz/standards.md) | Alle 9 unterstuetzten Standards im Detail |
| [Glossar](referenz/glossar.md) | Fachbegriffe von A bis Z |
| [Tastaturkuerzel](referenz/tastaturkuerzel.md) | Keyboard-Shortcuts und Command-Palette |
| [FAQ](referenz/faq.md) | Haeufig gestellte Fragen |

---

## Technische Eckdaten

| Eigenschaft | Wert |
|-------------|------|
| **Stack** | FastAPI + HTMX + Jinja2 + SQLite |
| **KI-Integration** | Claude AI (optional, per OAuth) |
| **Standards** | 9 (ISO 27001, 22301, 27005, 27017, 27018, 27035, NIS2, BSI, DSGVO) |
| **Controls** | 135 technische Pruefpunkte |
| **Domains** | 12 Sicherheitsbereiche |
| **AUDIT-CHECKs** | 2.042 semantische Anforderungen |
| **Deployment** | Docker Compose oder pip install |
| **Datenbank** | SQLite (WAL-Modus, lokal) |
| **Lizenz** | Apache-2.0 |

!!! warning "Rechtlicher Hinweis"
    ComplianceOS ist ein technisches Werkzeug zur Unterstuetzung von Compliance-Audits. Es ersetzt keine professionelle Rechts- oder Compliance-Beratung. Die Ergebnisse der automatisierten Pruefungen muessen von qualifiziertem Fachpersonal verifiziert werden.
