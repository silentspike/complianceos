# Executive Dashboard

Das Executive Dashboard bereitet Compliance-Daten fuer das Management auf — mit Fokus auf Risiko und Business Impact.

![Executive Dashboard](../screenshots/executive/executive-overview.png)

## Risiko-Matrix

Die Risiko-Matrix zeigt Findings auf einer 5x5-Matrix:

- **X-Achse:** Eintrittswahrscheinlichkeit (1-5)
- **Y-Achse:** Auswirkung / Impact (1-5)
- **Farbe:** Risiko-Kategorie (Gruen/Gelb/Orange/Rot)

Jeder Punkt repraesentiert ein Finding mit zugewiesener Risikobewertung.

## Business Impact

Fuer jedes bewertete Finding kann ein geschaetzter finanzieller Impact in Euro hinterlegt werden. Das Dashboard zeigt:

- Gesamt-Risikoexposition in Euro
- Top-10 Risiken nach finanziellem Impact
- Verteilung nach Risiko-Kategorie

## Compliance-Trends

Zeigt die Entwicklung des Compliance-Scores ueber mehrere Audit-Laeufe:

- Score-Verlauf als Liniendiagramm
- Findings-Entwicklung (steigend/fallend)
- Trend-Indikatoren pro Domain

## Risikobewertung erstellen

1. Oeffnen Sie ein Finding
2. Klicken Sie auf **Risiko bewerten**
3. Vergeben Sie:
   - **Eintrittswahrscheinlichkeit** (1-5)
   - **Auswirkung** (1-5)
   - **Geschaetzter Business Impact** (optional, in EUR)
   - **Risiko-Eigentuemer** (optional)
4. Klicken Sie auf **Speichern**

Der Risiko-Score wird automatisch berechnet (Wahrscheinlichkeit x Auswirkung).

!!! info "Wann bewerten?"
    Beginnen Sie mit den Major NCs — diese haben typischerweise den hoechsten
    Business Impact. Minor NCs und Observations koennen spaeter bewertet werden.
