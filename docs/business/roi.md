# ROI-Szenarien (illustrativ / synthetisch)

> **Wichtig:** Die folgenden sechs Szenarien sind **illustrative Modell-
> rechnungen** basierend auf typischen Enterprise-Audit-Zyklen. Tatsaechliche
> Einsparungen haengen von der organisatorischen Komplexitaet, der
> vorhandenen Compliance-Reife und der Integrations-Tiefe ab. Die Zahlen
> sind keine Zusage oder Garantie.

Die sechs Szenarien decken die typischen Groessen-Cluster und
Branchen-Profile ab: Mittelstand (ISO 27001), Grossunternehmen/Ministerium
(BSI IT-Grundschutz), KRITIS-Einzelbetrieb (NIS2), Krankenhaus (B3S +
DSGVO), Finanzdienstleister (BAIT/VAIT/ZAIT/DORA), Automotive-Zulieferer
(TISAX).

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

## Szenario 4 — Krankenhaus (Versorger > 30.000 Faelle/Jahr)

**Regulierungs-Kontext:** Branchenspezifischer Sicherheits-Standard
**B3S-Krankenhaus** (DKG/BSI-anerkannt) plus DSGVO-Pflichten fuer besonders
schuetzenswerte Gesundheitsdaten (Art. 9 DSGVO). Pruefungen alle zwei
Jahre durch eine pruefende Stelle.

**Ausgangslage ohne ComplianceOS:**

- IT-Sicherheitsteam mit 1,5 FTE plus Datenschutzbeauftragter (extern,
  20 % Auslastung)
- B3S-Anforderungen werden in einer Excel-Liste mit ueber 200 Pruefkriterien
  gepflegt; Querverweise zu DSGVO Art. 25/32 manuell
- KHZG-Foerderung erforderte parallele Nachweisfuehrung zu Sicherheits-
  Massnahmen (Foerdertatbestaende 1, 5, 10) — separate Excel
- Pruefungs-Vorbereitung: 60 Tage mit Dokumenten-Bundle und Interview-
  Vorbereitung der dezentralen Bereiche

**FTE-Aufwand pro 2-Jahres-Pruefzyklus (intern):** 22 FTE-Wochen

**Ausgangslage mit ComplianceOS:**

- B3S-Mapping als eigene Standard-Auspraegung (Cross-Standard-Mapping zu
  ISO 27001 und DSGVO automatisch)
- KHZG-relevante Massnahmen werden ueber Tags den entsprechenden
  Foerdertatbestaenden zugeordnet — ein Findings-Bestand, mehrere Reports
- Vorbereitungs-Dauer: 20 Tage mit Drift-Report seit der letzten Pruefung

**FTE-Aufwand pro 2-Jahres-Pruefzyklus (intern):** 8 FTE-Wochen

| Metrik | Vorher | Nachher | Einsparung |
|---|---|---|---|
| B3S-Pruefvorbereitung | 60 Tage | 20 Tage | -67 % |
| FTE-Wochen pro Zyklus | 22 | 8 | -14 FTE-Wochen |
| KHZG-Nachweis-Effort | separater Excel-Track | gleiche Findings, anderer Report-Filter | qualitativ entlastet |

**Anmerkung:** Pruefende Stellen nach B3S verlangen weiterhin originaer
gefuehrte Dokumentation pro Bereich (Notaufnahme, OP, Labor) — ComplianceOS
reduziert die Aggregations-Arbeit, nicht die fachliche Verantwortung der
Bereichsleitungen.

---

## Szenario 5 — Finanzdienstleister Mittelstand (1.500 Mitarbeiter)

**Regulierungs-Kontext:** **BAIT** (Banken), **VAIT** (Versicherungen),
**ZAIT** (Zahlungsdienste) — je nach Geschaeftsfeld kombinierbar — sowie
**DORA** (EU 2022/2554, Anwendung seit Januar 2025) mit verschaerften
Anforderungen an digitale operationale Resilienz, Threat-Led-Penetration-
Testing (TLPT) und ICT-Drittparteienregister.

**Ausgangslage ohne ComplianceOS:**

- 2-3 BAIT/VAIT-Pruefungen pro Jahr durch interne Revision plus jaehrliche
  Sonderpruefungen durch BaFin-beauftragte Auditoren
- DORA-Drittparteienregister wird in einer GRC-Insellandschaft gepflegt,
  Critical-ICT-Provider werden manuell gegen Vertraege abgeglichen
- Incident-Klassifikation gemaess DORA Art. 18 erfordert konsistente
  Severity-Bewertung — bisher uneinheitlich pro Pruefung
- TLPT-Vorbereitung jaehrlich: 8 Wochen Aufwand fuer Scope-Definition und
  Auditor-Onboarding

**FTE-Aufwand pro Jahr (intern, alle Pruefungen kumuliert):** 38 FTE-Wochen

**Ausgangslage mit ComplianceOS:**

- BAIT/VAIT/ZAIT als drei Standard-Auspraegungen mit Cross-Mapping zu
  ISO 27001 (gemeinsame Findings, Pruefer-spezifische Reports)
- DORA-Drittparteienregister als Erweiterung der Findings-Struktur, mit
  Tagging fuer Critical-ICT-Provider und automatischer Konsolidierung im
  jaehrlichen DORA-Selbstreport
- Incident-Klassifikation an die ComplianceOS-Severity-Logik angeschlossen
  (major / minor / observation), Audit-Trail pro Klassifikations-Entscheidung
- TLPT-Vorbereitung verkuerzt durch lebende Findings-Datenbank: 3 Wochen

**FTE-Aufwand pro Jahr (intern):** 16 FTE-Wochen

| Metrik | Vorher | Nachher | Einsparung |
|---|---|---|---|
| TLPT-Vorbereitung | 8 Wochen | 3 Wochen | -63 % |
| FTE-Wochen pro Jahr | 38 | 16 | -22 FTE-Wochen |
| Drittparteien-Register-Pflege | separates GRC-Tool | ein Findings-Bestand | qualitativ vereinheitlicht |

**Anmerkung:** ComplianceOS ersetzt weder die BaFin-Aufsicht noch
DORA-Pruefer. TLPT erfordert weiterhin akkreditierte Test-Provider und
ein eigenstaendiges Reporting an die Aufsichtsbehoerde.

---

## Szenario 6 — Automotive-Zulieferer (Tier-2, 800 Mitarbeiter)

**Regulierungs-Kontext:** **TISAX** (Trusted Information Security
Assessment Exchange) ist die Audit-Norm der deutschen Automobilindustrie,
gepflegt durch die ENX Association. Pruefniveaus sind **Level 2** (Self-
Assessment plus Plausibilitaets-Pruefung) und **Level 3** (vollstaendiger
Vor-Ort-Audit, erforderlich fuer hohe Verfuegbarkeits- oder
Geheimhaltungsanforderungen).

**Ausgangslage ohne ComplianceOS:**

- TISAX-Auditzyklus alle 3 Jahre, parallel laufende Anforderungen an ISO
  27001 (oft als Vorstufe oder begleitend)
- Self-Assessment basiert auf der ENX-Pflichtfragenliste mit ueber 110
  Anforderungen — gepflegt in Excel
- Reife-Beurteilung pro Anforderung (0-5) wird zwischen Audits mehrfach
  manuell aktualisiert
- Vor-Ort-Audit-Vorbereitung Level 3: 12 Wochen mit OEM-Liefer-Anforderungen
  (Hersteller-spezifische Zusatzklauseln)

**FTE-Aufwand pro Auditzyklus (intern):** 28 FTE-Wochen

**Ausgangslage mit ComplianceOS:**

- TISAX-Anforderungen werden als Standard-Auspraegung in der Control-Matrix
  gepflegt; Cross-Mapping zu ISO 27001 zeigt Doppelbelegung
- Reife-Beurteilung wird im Findings-Workflow gefuehrt (Severity entspricht
  Reife-Stufe), Audit-Trail pro Aenderung
- Vor-Ort-Audit-Vorbereitung Level 3: 4 Wochen, weil Drift-Report seit
  Self-Assessment automatisch erzeugt wird
- Hersteller-spezifische Zusatzklauseln werden via Tags / Custom-Controls
  als Erweiterung des TISAX-Basis-Sets gepflegt (siehe Customer-Override
  in der [Architektur-Doku](../architecture.md))

**FTE-Aufwand pro Auditzyklus (intern):** 10 FTE-Wochen

| Metrik | Vorher | Nachher | Einsparung |
|---|---|---|---|
| Vor-Ort-Audit-Vorbereitung | 12 Wochen | 4 Wochen | -67 % |
| FTE-Wochen pro Zyklus | 28 | 10 | -18 FTE-Wochen |
| Reife-Beurteilung | mehrfach manuell aktualisiert | Findings-Workflow mit Audit-Trail | qualitativ verbessert |

**Anmerkung:** Level-3-Pruefungen erfordern weiterhin eine ENX-akkreditierte
Pruefstelle und einen Vor-Ort-Termin. ComplianceOS reduziert die interne
Vorbereitungszeit, nicht die regulatorische Pflicht zur externen Pruefung.

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
