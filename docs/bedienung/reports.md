# Reports

ComplianceOS bietet umfangreiche Report- und Analysefunktionen: Audit-Reports, Drift-Detection, Cross-Standard-Mapping und Matrix-Analytik. Jeder Report-Typ richtet sich an eine andere Zielgruppe und Fragestellung.

<figure class="screenshot" markdown>
![Reports Übersicht](../screenshots/reports/reports-overview.png)
<figcaption>Reports: Report-Generator, Drift-Detection und generierte Reports in der Übersicht</figcaption>
</figure>

---

## Audit-Report

Der Audit-Report fasst die Ergebnisse eines Audit-Laufs in einem strukturierten Dokument zusammen — geeignet für Management-Präsentationen, externe Auditoren und Compliance-Nachweise.

### Report erstellen

1. Navigieren Sie zu **Reports** in der Seitenleiste
2. Wählen Sie im Dropdown den gewünschten **Audit-Lauf**
3. Klicken Sie auf **Report generieren**
4. Der Report wird generiert und in der Liste angezeigt

### Report-Inhalt

Jeder Audit-Report enthält:

| Abschnitt | Inhalt |
|-----------|--------|
| **Executive Summary** | Überblick für die Geschäftsführung mit Gesamt-Score und Key-Findings |
| **Scope** | Welche Standards, Domains und Controls geprüft wurden |
| **Ergebnisse nach Severity** | Aufschlüsselung aller Findings nach Schweregrad |
| **Domain-Analyse** | Detaillierte Ergebnisse pro Sicherheitsbereich |
| **Top-Findings** | Die kritischsten Abweichungen mit Empfehlungen |
| **Empfehlungen** | Priorisierte Handlungsempfehlungen |
| **Statistiken** | Controls geprüft, Compliance-Grad, Trend |

### Report-Detail

<figure class="screenshot" markdown>
![Report Detail](../screenshots/reports/report-detail.png)
<figcaption>Generierter Audit-Report: Executive Summary, Ergebnisse nach Severity und Domain-Analyse</figcaption>
</figure>

Klicken Sie in der Reports-Liste auf einen generierten Report um die Detailansicht zu öffnen. Der Report wird als formatiertes Markdown dargestellt.

---

## Drift-Detection

Die Drift-Detection vergleicht zwei Audit-Läufe und identifiziert Veränderungen im Compliance-Zustand. So erkennen Sie Verbesserungen, Regressionen und stehende Findings.

### Drift-Report erstellen

1. Im Bereich **Drift Detection** wählen Sie:
      - **Baseline**: Der ältere Audit-Lauf (Referenzpunkt)
      - **Aktuell**: Der neuere Audit-Lauf (Vergleichspunkt)
2. Klicken Sie auf **Vergleichen**

### Drift-Kategorien

Der Drift-Report kategorisiert alle Findings:

| Kategorie | Bedeutung | Farbe | Aktion |
|-----------|-----------|-------|--------|
| **Neue Findings** | Im aktuellen Audit erstmals aufgetreten | Rot | Neue Massnahmen planen |
| **Behobene Findings** | Im Baseline vorhanden, jetzt nicht mehr | Grün | Erfolg der Massnahmen bestätigt |
| **Unveränderte Findings** | In beiden Audits vorhanden | Grau | Massnahmen beschleunigen |
| **Verschlechterte Findings** | Severity hat sich erhöht | Dunkelrot | Sofort eskalieren |

### Drift-Metriken

Zusätzlich zeigt der Drift-Report:

- **Score-Vergleich**: Compliance-Score Baseline vs. Aktuell
- **Score-Delta**: Verbesserung oder Verschlechterung in Prozentpunkten
- **Domain-Trends**: Welche Domains sich verbessert oder verschlechtert haben
- **Regression-Count**: Anzahl neuer oder verschlechterter Findings

!!! warning "Regressionen"
    Neue Major NCs nach einem vorherigen Audit deuten auf **Regressionen** hin — Sicherheitsmassnahmen die wieder entfernt oder unwirksam geworden sind. Diese erfordern sofortige Aufmerksamkeit.

!!! tip "Regelmässige Drift-Checks"
    Führen Sie nach jedem Audit einen Drift-Vergleich zum vorherigen Lauf durch. So behalten Sie die Entwicklung Ihres Compliance-Zustands im Blick und erkennen negative Trends frühzeitig.

---

## Cross-Standard-Mapping

Das Cross-Standard-Mapping visualisiert die Beziehungen und Überschneidungen zwischen den 9 unterstützten Standards.

<figure class="screenshot" markdown>
![Cross-Standard Mapping](../screenshots/reports/cross-standard.png)
<figcaption>Cross-Standard: Netzwerk-Graph der Standard-Beziehungen, Overlap-Matrix und Readiness-Rechner</figcaption>
</figure>

### Netzwerk-Graph

Der interaktive **Netzwerk-Graph** zeigt:

- **Knoten**: Jeder Standard als Kreis (Grösse = Anzahl Controls)
- **Kanten**: Verbindungen zwischen Standards mit gemeinsamen Controls
- **Stärke**: Dicke der Kante = Anzahl geteilter Controls

So erkennen Sie auf einen Blick welche Standards stark miteinander verknüpft sind und wo Synergien bei der Implementierung bestehen.

### Overlap-Matrix

Die **Overlap-Matrix** zeigt in einer Tabelle:

- Zeilen und Spalten: Alle 9 Standards
- Zellen: Anzahl gemeinsamer Controls
- Diagonale: Gesamtzahl Controls des Standards

### Readiness-Rechner

Der **Readiness-Rechner** beantwortet die Frage: "Wenn ich Standard X erfülle, wie weit bin ich bei Standard Y?"

- Wählen Sie einen Quell-Standard
- Sehen Sie den Abdeckungsgrad für alle anderen Standards
- Planen Sie die effizienteste Reihenfolge für Multi-Standard-Compliance

!!! tip "Synergien nutzen"
    ISO 27001 teilt viele Controls mit NIS2 und BSI IT-Grundschutz. Beginnen Sie mit dem Standard der die meisten Überschneidungen bietet — so erreichen Sie mit dem geringsten Aufwand die höchste Abdeckung.

---

## Matrix-Analytik

Die Matrix-Analytik bietet erweiterte Visualisierungen zur Control-Verteilung und Standard-Abdeckung.

<figure class="screenshot" markdown>
![Matrix-Analytik](../screenshots/reports/matrix-analytik.png)
<figcaption>Matrix-Analytik: Sankey-Diagramm, Pie-Chart, Automation-Topography und Coverage-Matrix</figcaption>
</figure>

### Visualisierungen

| Visualisierung | Beschreibung |
|----------------|-------------|
| **Sankey-Diagramm** | Zeigt den Fluss von Standards zu Domains — welcher Standard welche Domains abdeckt |
| **Pie-Chart** | Verteilung der Controls nach Verifikationsmethode (Automated, Hybrid, Manual) |
| **Automation-Topography** | Welche Domains den höchsten Automatisierungsgrad haben |
| **Coverage-Matrix** | Heatmap: Standards (Zeilen) vs. Domains (Spalten) — Anzahl Controls pro Zelle |

### Coverage-Matrix lesen

Die Coverage-Matrix ist besonders wertvoll für die Audit-Planung:

- **Dunkle Zellen**: Viele Controls — hoher Prüfaufwand in dieser Kombination
- **Helle Zellen**: Wenige Controls
- **Leere Zellen**: Kein Control dieses Standards in dieser Domain
- **Zeilen-Summe**: Gesamtzahl Controls des Standards
- **Spalten-Summe**: Gesamtzahl Controls in der Domain

---

## Generierte Reports verwalten

Alle generierten Reports werden in der Datenbank gespeichert:

| Feld | Beschreibung |
|------|-------------|
| **Titel** | Report-Bezeichnung |
| **Typ** | Audit-Report oder Drift-Report |
| **Erstellungsdatum** | Wann der Report generiert wurde |
| **Basis-Audit** | Welcher Audit-Lauf als Grundlage diente |

Reports können jederzeit wieder geöffnet und eingesehen werden.

---

## Tipps für effektive Reports

!!! tip "Für das Management"
    Generieren Sie einen Audit-Report nach jedem Vollaudit. Der Executive Summary eignet sich als Grundlage für Management-Präsentationen und zeigt den Compliance-Status auf einen Blick.

!!! tip "Für externe Auditoren"
    Stellen Sie externen Auditoren den vollständigen Audit-Report plus die Cross-Standard-Matrix zur Verfügung. So sehen Auditoren sofort welche Standards abgedeckt sind und wo die Schwerpunkte liegen.

!!! tip "Für die Planung"
    Nutzen Sie die Matrix-Analytik und den Readiness-Rechner um die effizienteste Reihenfolge für die Implementierung weiterer Standards zu bestimmen.

---

## Video: Drift-Detection

<div class="video-container" markdown>
<video controls width="100%">
  <source src="../videos/drift-detection.mp4" type="video/mp4">
  Ihr Browser unterstützt kein Video. <a href="../videos/drift-detection.mp4">Video herunterladen</a>.
</video>
</div>

Das Video zeigt die Drift-Detection und Report-Funktionen: Vom Reports-Bereich über die Drift-Analyse zweier Audit-Läufe bis zur Cross-Standard-Matrix und Matrix-Analytik.
