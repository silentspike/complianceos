# ROI-Szenarien (illustrativ / synthetisch)

> **Wichtig:** Die folgenden drei Szenarien sind **illustrative Modell-
> rechnungen** basierend auf typischen Enterprise-Audit-Zyklen. Tatsaechliche
> Einsparungen haengen von der organisatorischen Komplexitaet, der
> vorhandenen Compliance-Reife und der Integrations-Tiefe ab. Die Zahlen
> sind keine Zusage oder Garantie.

Die drei Szenarien decken die typischen Groessen-Cluster ab: Mittelstand,
Grossunternehmen/Ministerium, KRITIS-Einzelbetrieb.

---

## Szenario 1 — Mittelstaendler (500 Mitarbeiter)

**Ausgangslage ohne ComplianceOS:**

- ISO 27001:2022 Zertifizierung (Rezertifizierung alle 3 Jahre, Ueberwachungs-
  audits jaehrlich)
- 1 CISO + 2 Compliance-Teilzeitstellen (insgesamt 2,0 FTE)
- Audit-Vorbereitung: 90 Tage vor Audit-Termin mit Dokumenten-Sammeln,
  Findings-Tracking in Excel, Interview-Koordination
- Externer Auditor-Aufwand: 10 Personentage (Stage 1 + Stage 2)

**FTE-Aufwand pro Audit-Zyklus (intern):** 15 FTE-Wochen

**Ausgangslage mit ComplianceOS:**

- Kontinuierliche Findings-Pflege (Drift-Detection) zwischen Audit-Zyklen
- Automatisierte Evidence-Extraktion aus Dokumenten-Uploads
- Dashboard-basierter ISB-Report statt manuelle Aggregation
- Audit-Vorbereitung: 30 Tage mit iterativer Gap-Analyse

**FTE-Aufwand pro Audit-Zyklus (intern):** 5 FTE-Wochen

| Metrik | Vorher | Nachher | Einsparung |
|---|---|---|---|
| Audit-Vorbereitungszeit | 90 Tage | 30 Tage | -67 % |
| Interne FTE-Wochen pro Zyklus | 15 | 5 | -10 FTE-Wochen |
| Tool-Kosten | 0 (Excel) | ComplianceOS-Lizenz | — |

**Anmerkung:** Die externe Auditor-Zeit (10 Personentage) bleibt unveraendert
— ComplianceOS ersetzt keinen akkreditierten Auditor.

---

## Szenario 2 — Ministerium / Grossbehoerde (10.000 Mitarbeiter)

**Ausgangslage ohne ComplianceOS:**

- BSI IT-Grundschutz mit etwa 60 Bausteinen im Verbund
- ISB-Team mit 4-6 FTE, dazu dezentrale IT-Sicherheitsbeauftragte
- Audit-Zyklus: 6-Monats-Rhythmus fuer interne Gap-Analyse, 3 Jahre fuer
  externe Rezertifizierung
- Schutzbedarfsfeststellung pro System, manuelle Fortschreibung in Excel-
  Matrizen

**FTE-Aufwand pro 6-Monats-Zyklus (intern):** 45 FTE-Wochen

**Ausgangslage mit ComplianceOS:**

- Baustein-basierte Modellierung direkt im Tool
- Cross-Standard-Mapping (IT-Grundschutz + ISO 27001) spart doppelte Arbeit
- Findings-Drift-Detection identifiziert Regressionen zwischen Zyklen
- Automatisierter BSI-Report-Export aus Findings-Datenbank

**FTE-Aufwand pro 2-Monats-Zyklus (intern):** 15 FTE-Wochen

| Metrik | Vorher | Nachher | Einsparung |
|---|---|---|---|
| Audit-Zyklus-Dauer | 6 Monate | 2 Monate | -67 % |
| FTE-Wochen pro Zyklus | 45 | 15 | -30 FTE-Wochen |
| Kurz-Zyklus-Faehigkeit | monatlicher Gap-Check unrealistisch | moeglich | neu |

**Anmerkung:** Der kuerzere Zyklus erlaubt agilere Priorisierung — kritische
Lucken werden Wochen statt Monate frueher sichtbar.

---

## Szenario 3 — KRITIS-Einzelbetrieb

**Ausgangslage ohne ComplianceOS:**

- NIS2-Pflichten mit 4 definierten Audits pro Jahr (kurzfristig und angekuendigt)
- Typisch 20 Personentage interner Aufwand pro Audit (Vorbereitung,
  Durchfuehrung, Nachbereitung)
- Jahres-Gesamt: 4 x 20 = 80 Personentage (ca. 16 FTE-Wochen)

**Ausgangslage mit ComplianceOS:**

- Vorhandene Audit-Daten und Drift-Zustand sind jederzeit aktuell gehalten
- Audit-Vorbereitung reduziert sich auf Report-Export + Diff-Review
- Typisch 7 Personentage interner Aufwand pro Audit

**Jahres-Aufwand mit ComplianceOS:** 4 x 7 = 28 Personentage (ca. 5,6
FTE-Wochen)

| Metrik | Vorher | Nachher | Einsparung |
|---|---|---|---|
| Audits pro Jahr | 4 | 4 | gleich |
| Personentage pro Audit | 20 | 7 | -65 % |
| Jahres-FTE-Wochen | 16 | 5,6 | -10,4 FTE-Wochen |

**Anmerkung:** Die 4 NIS2-Audits bleiben Pflicht — ComplianceOS reduziert
den internen Aufwand pro Audit, nicht die Audit-Frequenz.

---

## Typische Amortisation

Die Lizenzkosten fuer ComplianceOS amortisieren sich bei allen drei
Szenarien ueber die eingesparten FTE-Wochen (kalkulierbar ca. 3.000 EUR pro
FTE-Woche Vollkosten in Deutschland).

Fuer konkrete Lizenz-Angebote und individuelle ROI-Rechnungen anhand Ihrer
Organisation bitte ueber das [Evaluation-Request-Template](https://github.com/silentspike/complianceos/issues/new?template=evaluation_request.yml)
Kontakt aufnehmen.

---

## Disclaimer

Diese Szenarien basieren auf Annahmen ueber typische Enterprise-Audit-Zyklen.
Die tatsaechlichen Einsparungen in einer gegebenen Organisation haengen von:

- Bestehender Compliance-Reife und vorhandenen Dokumenten
- Anzahl parallel zu erfuellender Standards
- Bereits vorhandener Tool-Landschaft (GRC-Systeme, ITSM)
- Qualitaet und Struktur der zugrundeliegenden Dokumenten-Landschaft

ComplianceOS ist ein Werkzeug zur Unterstuetzung der Compliance-Arbeit —
es ersetzt weder qualifizierte Pruefer noch eigene Expertise in der
Organisation.
