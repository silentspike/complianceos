# Executive Dashboard

Das Executive Dashboard bereitet Compliance-Daten fuer die Geschaeftsfuehrung auf — mit Fokus auf Risikobewertung, finanziellen Business Impact und Compliance-Trends.

<figure class="screenshot" markdown>
![Executive Dashboard](../screenshots/executive/executive-overview.png)
<figcaption>Executive Dashboard: Risk Score, Gesamt-Risikoexposition, 5x5-Heatmap, KPI-Trends und Domain-Risiken</figcaption>
</figure>

---

## Ueberblick

Das Executive Dashboard besteht aus mehreren Bereichen:

| Bereich | Beschreibung |
|---------|-------------|
| **Risk Score** | Gewichteter Gesamt-Risikowert |
| **Risikoexposition** | Geschaetzter finanzieller Gesamtimpact in EUR |
| **Risiko-Heatmap** | 5x5-Matrix: Wahrscheinlichkeit vs. Auswirkung |
| **KPI-Trends** | Score-Entwicklung ueber mehrere Audit-Laeufe |
| **Domain-Risiken** | Risiko-Bewertung pro Sicherheitsbereich |
| **Top-Risiken** | Die kritischsten Findings nach Business Impact |

---

## Risk Score

Der **Risk Score** ist eine einzelne Zahl die das Gesamtrisiko Ihrer Organisation zusammenfasst. Er wird aus allen bewerteten Findings berechnet:

- **Formel**: Gewichteter Durchschnitt aus (Wahrscheinlichkeit x Auswirkung) aller bewerteten Findings
- **Skala**: 0.0 (kein Risiko) bis 25.0 (maximales Risiko)
- **Farbe**: Gruen (0-5), Gelb (5-10), Orange (10-15), Rot (15-25)

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
| 1-4 | Niedrig | Gruen | Akzeptables Risiko, regelmaessig ueberwachen |
| 5-9 | Mittel | Gelb | Massnahmen planen, Risiko reduzieren |
| 10-14 | Hoch | Orange | Priorisierte Massnahmen erforderlich |
| 15-25 | Kritisch | Rot | Sofortige Massnahmen, Eskalation an Management |

### Heatmap lesen

- **Jeder Punkt** repraesentiert ein Finding mit Risikobewertung
- **Position**: Zeigt Wahrscheinlichkeit und Auswirkung
- **Farbe der Zelle**: Risiko-Kategorie
- **Haeufung oben-rechts**: Kritischer Bereich — viele hochriskante Findings

---

## KPI-Trends

Der Bereich **Compliance-Trends** zeigt die Entwicklung ueber mehrere Audit-Laeufe:

| Trend | Beschreibung |
|-------|-------------|
| **Score-Verlauf** | Compliance-Score als Linie ueber die Zeit |
| **Findings-Trend** | Anzahl offener Findings pro Audit-Lauf |
| **Trend-Pfeile** | Aufwaerts (Verbesserung) oder Abwaerts (Verschlechterung) |

Die Trend-Daten helfen bei der Beantwortung der Management-Frage: "Verbessert sich unsere Compliance-Lage oder verschlechtert sie sich?"

---

## Domain-Risiken

Fuer jede der 12 Domains wird der aggregierte Risikowert angezeigt:

- **Balkendiagramm** mit Risiko-Score pro Domain
- **Farbcodierung** nach Risiko-Kategorie
- **Sortierung** nach Risikohoehe (hoechstes Risiko zuerst)

So identifiziert das Management auf einen Blick welche Sicherheitsbereiche die groesste Aufmerksamkeit benoetigen.

---

## Risikobewertung erstellen

### Aus der Finding-Detailansicht

1. Oeffnen Sie ein Finding in der Detailansicht
2. Klicken Sie auf **Risiko bewerten**
3. Vergeben Sie:

| Feld | Werte | Beschreibung |
|------|-------|-------------|
| **Eintrittswahrscheinlichkeit** | 1-5 | Wie wahrscheinlich ist der Eintritt? |
| **Auswirkung** | 1-5 | Wie schwer waere der Schaden? |
| **Business Impact** | EUR (optional) | Geschaetzter finanzieller Schaden |
| **Risiko-Eigentuemer** | Person (optional) | Wer ist fuer das Risiko verantwortlich? |

4. Klicken Sie auf **Speichern**

Der **Risiko-Score** wird automatisch berechnet: Wahrscheinlichkeit x Auswirkung.

### Bewertungsskala

**Eintrittswahrscheinlichkeit:**

| Wert | Stufe | Beschreibung |
|------|-------|-------------|
| 1 | Selten | Einmal in 5+ Jahren |
| 2 | Unwahrscheinlich | Einmal in 2-5 Jahren |
| 3 | Moeglich | Einmal pro Jahr |
| 4 | Wahrscheinlich | Mehrmals pro Jahr |
| 5 | Sehr wahrscheinlich | Monatlich oder oefter |

**Auswirkung:**

| Wert | Stufe | Beschreibung |
|------|-------|-------------|
| 1 | Gering | Minimaler Schaden, intern behebbar |
| 2 | Niedrig | Begrenzter Schaden, kurze Wiederherstellung |
| 3 | Mittel | Spuerbarer Schaden, Tage fuer Wiederherstellung |
| 4 | Hoch | Erheblicher Schaden, Wochen fuer Wiederherstellung |
| 5 | Katastrophal | Existenzbedrohend, Datenverlust, regulatorische Konsequenzen |

---

## Tipps fuer das Executive Dashboard

!!! info "Wann bewerten?"
    Beginnen Sie mit den **Major NCs** — diese haben typischerweise den hoechsten Business Impact. Minor NCs und Observations koennen in einer zweiten Runde bewertet werden.

!!! tip "Fuer Board-Praesentationen"
    Das Executive Dashboard eignet sich ideal fuer Board-Praesentationen: Risk Score, Heatmap und Trends auf einen Blick. Kombinieren Sie es mit einem [Audit-Report](reports.md) fuer die Details.

!!! tip "Risiko-Eigentuemer"
    Weisen Sie jedem hochriskanten Finding einen Risiko-Eigentuemer zu. So ist klar wer fuer die Risikominimierung verantwortlich ist und an wen eskaliert wird.

!!! tip "Regelmaessige Updates"
    Aktualisieren Sie die Risikobewertungen nach jedem Audit. Der Trend zeigt dann ob Ihre Massnahmen die Gesamtrisikolage verbessern.
