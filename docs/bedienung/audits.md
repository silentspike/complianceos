# Audits

Audits sind der Kern von ComplianceOS. Sie pruefen Ihre Infrastruktur systematisch gegen Compliance-Controls.

![Audits Uebersicht](../screenshots/audits/audits-overview.png)

## Audit starten

1. Navigieren Sie zu **Audits** in der Seitenleiste
2. Waehlen Sie den Modus:
   - **Vollaudit:** Prueft alle 135 Controls in allen 12 Domains
   - **Domain-Audit:** Prueft nur eine spezifische Domain (z.B. CRYPTO, ACCESS)
3. Klicken Sie auf **Audit starten**

!!! info "Audit-Dauer"
    - **Vollaudit:** 1-5 Minuten (abhaengig von der Systemleistung)
    - **Domain-Audit:** Wenige Sekunden

## Fortschritt

Waehrend der Audit laeuft, sehen Sie:

- Aktueller Fortschritt (x von y Controls geprueft)
- Die aktuelle Domain, die geprueft wird
- Bereits gefundene Findings in Echtzeit

## Audit-Ergebnis

Nach Abschluss zeigt die Detail-Ansicht:

![Audit Detail](../screenshots/audits/audit-detail.png)

- **Zusammenfassung:** Gesamtzahl Findings nach Severity
- **Domain-Aufschluesselung:** Ergebnisse pro Domain
- **Findings-Liste:** Alle identifizierten Abweichungen
- **Zeitstempel:** Start- und Endzeitpunkt

## Audit-Vergleich

Sie koennen zwei Audit-Laeufe miteinander vergleichen, um Veraenderungen zu erkennen:

1. Oeffnen Sie einen Audit-Lauf
2. Klicken Sie auf **Vergleichen**
3. Waehlen Sie einen frueheren Audit-Lauf

![Audit Vergleich](../screenshots/audits/audit-compare.png)

Die Vergleichsansicht zeigt:
- Neue Findings (im aktuellen, aber nicht im frueheren Audit)
- Behobene Findings (im frueheren, aber nicht im aktuellen Audit)
- Unveraenderte Findings

## Geplante Audits

Unter **Einstellungen > Zeitplaene** koennen Sie automatische Audits einrichten:

- **Taeglich:** Jeden Tag zu einer bestimmten Uhrzeit
- **Woechentlich:** Einmal pro Woche
- **Monatlich:** Einmal pro Monat

!!! warning "Voraussetzung"
    Geplante Audits funktionieren nur, solange der ComplianceOS-Container laeuft.
