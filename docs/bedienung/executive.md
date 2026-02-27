# Executive Dashboard

Das Executive Dashboard bereitet Compliance-Daten für die Geschäftsführung auf — mit Fokus auf Risikobewertung, finanziellen Business Impact und Compliance-Trends.

<figure class="screenshot" markdown>
![Executive Dashboard](../screenshots/executive/executive-overview.png)
<figcaption>Executive Dashboard: Risk Score, Gesamt-Risikoexposition, 5x5-Heatmap, KPI-Trends und Domain-Risiken</figcaption>
</figure>

---

## Überblick

Das Executive Dashboard besteht aus mehreren Bereichen:

| Bereich | Beschreibung |
|---------|-------------|
| **Risk Score** | Gewichteter Gesamt-Risikowert |
| **Risikoexposition** | Geschätzter finanzieller Gesamtimpact in EUR |
| **Risiko-Heatmap** | 5x5-Matrix: Wahrscheinlichkeit vs. Auswirkung |
| **KPI-Trends** | Score-Entwicklung über mehrere Audit-Läufe |
| **Domain-Risiken** | Risiko-Bewertung pro Sicherheitsbereich |
| **Top-Risiken** | Die kritischsten Findings nach Business Impact |

---

## Risk Score

Der **Risk Score** ist eine einzelne Zahl die das Gesamtrisiko Ihrer Organisation zusammenfasst. Er wird aus allen bewerteten Findings berechnet:

- **Formel**: Gewichteter Durchschnitt aus (Wahrscheinlichkeit x Auswirkung) aller bewerteten Findings
- **Skala**: 0.0 (kein Risiko) bis 25.0 (maximales Risiko)
- **Farbe**: Grün (0-5), Gelb (5-10), Orange (10-15), Rot (15-25)

Darunter zeigt die **Gesamt-Risikoexposition** den summierten finanziellen Business Impact aller bewerteten Findings in EUR.

---

## Risiko-Heatmap (5x5-Matrix)

Die Risiko-Heatmap visualisiert alle bewerteten Findings auf einer 5x5-Matrix:

### Achsen

| Achse | Werte | Bedeutung |
|-------|-------|-----------|
| **X-Achse** | 1-5 | Eintrittswahrscheinlichkeit (selten bis sehr wahrscheinlich) |
| **Y-Achse** | 1-5 | Auswirkung / Impact (gering bis katastrophal) |

### Risiko-Kategorien

| Risiko-Score | Kategorie | Farbe | Beschreibung |
|-------------|-----------|-------|-------------|
| 1-4 | Niedrig | Grün | Akzeptables Risiko, regelmässig überwachen |
| 5-9 | Mittel | Gelb | Massnahmen planen, Risiko reduzieren |
| 10-14 | Hoch | Orange | Priorisierte Massnahmen erforderlich |
| 15-25 | Kritisch | Rot | Sofortige Massnahmen, Eskalation an Management |

### Heatmap lesen

- **Jeder Punkt** repräsentiert ein Finding mit Risikobewertung
- **Position**: Zeigt Wahrscheinlichkeit und Auswirkung
- **Farbe der Zelle**: Risiko-Kategorie
- **Häufung oben-rechts**: Kritischer Bereich — viele hochriskante Findings

---

## KPI-Trends

Der Bereich **Compliance-Trends** zeigt die Entwicklung über mehrere Audit-Läufe:

| Trend | Beschreibung |
|-------|-------------|
| **Score-Verlauf** | Compliance-Score als Linie über die Zeit |
| **Findings-Trend** | Anzahl offener Findings pro Audit-Lauf |
| **Trend-Pfeile** | Aufwärts (Verbesserung) oder Abwärts (Verschlechterung) |

Die Trend-Daten helfen bei der Beantwortung der Management-Frage: "Verbessert sich unsere Compliance-Lage oder verschlechtert sie sich?"

---

## Domain-Risiken

Für jede der 12 Domains wird der aggregierte Risikowert angezeigt:

- **Balkendiagramm** mit Risiko-Score pro Domain
- **Farbcodierung** nach Risiko-Kategorie
- **Sortierung** nach Risikohöhe (höchstes Risiko zuerst)

So identifiziert das Management auf einen Blick welche Sicherheitsbereiche die grösste Aufmerksamkeit benötigen.

---

## Risikobewertung erstellen

### Aus der Finding-Detailansicht

1. Öffnen Sie ein Finding in der Detailansicht
2. Klicken Sie auf **Risiko bewerten**
3. Vergeben Sie:

| Feld | Werte | Beschreibung |
|------|-------|-------------|
| **Eintrittswahrscheinlichkeit** | 1-5 | Wie wahrscheinlich ist der Eintritt? |
| **Auswirkung** | 1-5 | Wie schwer wäre der Schaden? |
| **Business Impact** | EUR (optional) | Geschätzter finanzieller Schaden |
| **Risiko-Eigentümer** | Person (optional) | Wer ist für das Risiko verantwortlich? |

4. Klicken Sie auf **Speichern**

Der **Risiko-Score** wird automatisch berechnet: Wahrscheinlichkeit x Auswirkung.

### Bewertungsskala

**Eintrittswahrscheinlichkeit:**

| Wert | Stufe | Beschreibung |
|------|-------|-------------|
| 1 | Selten | Einmal in 5+ Jahren |
| 2 | Unwahrscheinlich | Einmal in 2-5 Jahren |
| 3 | Möglich | Einmal pro Jahr |
| 4 | Wahrscheinlich | Mehrmals pro Jahr |
| 5 | Sehr wahrscheinlich | Monatlich oder öfter |

**Auswirkung:**

| Wert | Stufe | Beschreibung |
|------|-------|-------------|
| 1 | Gering | Minimaler Schaden, intern behebbar |
| 2 | Niedrig | Begrenzter Schaden, kurze Wiederherstellung |
| 3 | Mittel | Spürbarer Schaden, Tage für Wiederherstellung |
| 4 | Hoch | Erheblicher Schaden, Wochen für Wiederherstellung |
| 5 | Katastrophal | Existenzbedrohend, Datenverlust, regulatorische Konsequenzen |

---

## Tipps für das Executive Dashboard

!!! info "Wann bewerten?"
    Beginnen Sie mit den **Major NCs** — diese haben typischerweise den höchsten Business Impact. Minor NCs und Observations können in einer zweiten Runde bewertet werden.

!!! tip "Für Board-Präsentationen"
    Das Executive Dashboard eignet sich ideal für Board-Präsentationen: Risk Score, Heatmap und Trends auf einen Blick. Kombinieren Sie es mit einem [Audit-Report](reports.md) für die Details.

!!! tip "Risiko-Eigentümer"
    Weisen Sie jedem hochriskanten Finding einen Risiko-Eigentümer zu. So ist klar wer für die Risikominimierung verantwortlich ist und an wen eskaliert wird.

!!! tip "Regelmässige Updates"
    Aktualisieren Sie die Risikobewertungen nach jedem Audit. Der Trend zeigt dann ob Ihre Massnahmen die Gesamtrisikolage verbessern.
