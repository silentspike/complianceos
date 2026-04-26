# DORA — Digital Operational Resilience Act

> **Kontext:** Die EU-Verordnung 2022/2554 (DORA) ist seit dem 17. Januar
> 2025 unmittelbar anwendbar. Sie etabliert eine harmonisierte Regelung
> fuer digitale operationale Resilienz im Finanzsektor und greift in
> nationale Anforderungen wie BAIT/VAIT/ZAIT mit hoeherem Vorrang ein.

---

## Geltungsbereich

DORA gilt fuer **Finanzunternehmen** im Sinne von Art. 2 — darunter
Kreditinstitute, Wertpapierfirmen, Zahlungsinstitute, E-Geld-Institute,
Versicherungsunternehmen, zentrale Gegenparteien, Handelsplaetze und
zentrale Verwahrer. Erfasst sind ebenfalls **kritische IKT-Drittdienst-
leister** (z.B. grosse Cloud-Anbieter), die einer eigenen EU-Aufsicht
unterliegen.

Es gibt Erleichterungen fuer Kleinst-Unternehmen und definierte
Schwellenwerte fuer einzelne Pflichten — die Grundpflichten zum
ICT-Risikomanagement gelten jedoch grundsaetzlich.

---

## Fuenf Saeulen

DORA strukturiert die Anforderungen entlang fuenf Themenbloecken:

| Saeule | Inhalt |
|---|---|
| **1. ICT-Risikomanagement-Framework** | Governance, Strategie, Schutzbedarfsfeststellung, kontinuierliches Risiko-Monitoring (Art. 5–16) |
| **2. Incident-Reporting** | Klassifikation, Meldepflichten, Eskalationsschwellen (Art. 17–23) |
| **3. Resilience-Testing** | Regelmaessige Tests inkl. Threat-Led-Penetration-Testing (TLPT) fuer kritische Funktionen (Art. 24–27) |
| **4. ICT-Drittparteien-Management** | Register, Vertragsanforderungen, Konzentrationsrisiken (Art. 28–44) |
| **5. Informationsaustausch** | Branchenuebergreifende Threat-Intelligence-Plattformen (Art. 45) |

---

## Incident-Klassifikation (Art. 18)

DORA verlangt eine konsistente Klassifikation von ICT-Vorfaellen anhand
quantitativer und qualitativer Kriterien. Die Delegierte Verordnung der
EU-Kommission (RTS) konkretisiert sieben Klassifikations-Kriterien:

1. Anzahl und Bedeutung betroffener Kunden bzw. Gegenparteien
2. Reputationsfolgen
3. Dauer und Ausweitung des Vorfalls
4. Geographische Reichweite
5. Datenverlust (Vertraulichkeit, Integritaet, Verfuegbarkeit)
6. Schwerwiegendheit des Auswirkens auf wirtschaftliche Funktionen
7. Wirtschaftlicher Schaden

Ein Vorfall gilt als **major** wenn definierte Schwellwerte ueber-
schritten werden. Major-Vorfaelle sind nach DORA-Standardfristen zu
melden.

---

## Threat-Led-Penetration-Testing (Art. 26-27)

TLPT ist eine **Pflicht** fuer signifikante Finanzunternehmen. Es
unterscheidet sich von gewoehnlichem Pen-Testing durch:

- **Threat-Intelligence-basiertes Szenario** (TIBER-EU-Methodik)
- **Live-Production-Testing** statt Test-Umgebung
- **Akkreditierte Test-Provider** (TLPT-Authority pro Mitgliedstaat)
- **Dreijaehrlicher Mindestturnus** mit Aufsichts-Beobachtung
- **Vertrauliche Behandlung** der Befunde (begrenzter Adressatenkreis)

In Deutschland ist die Bundesbank gemeinsam mit der BaFin die zustaendige
TLPT-Authority.

---

## ICT-Drittparteien-Register (Art. 28)

Finanzunternehmen muessen ein **Register aller ICT-Vertragsbeziehungen**
fuehren mit Pflichtfeldern wie:

- Identifikation des Dienstleisters (LEI)
- Beschreibung des bezogenen Dienstes (kritisch / wichtig / sonstig)
- Datenkategorien
- Standorte der Datenverarbeitung
- Sub-Outsourcing-Ketten

Bei **kritischen ICT-Drittdienstleistern** (separat designiert auf EU-
Ebene durch die ESAs) gelten erweiterte Vertragsanforderungen und
Substitutions-Strategien.

---

## Meldefristen

DORA harmonisiert die Frueh-Warnung und Folge-Meldungen. Die finalen
Fristen ergeben sich aus den RTS / ITS:

| Stufe | Frist |
|---|---|
| Initiale Meldung (major incident) | innerhalb weniger Stunden nach Klassifikation |
| Zwischen-Meldung | innerhalb von 72 Stunden |
| Abschluss-Bericht | binnen eines Monats nach Vorfalls-Behebung |

In Deutschland: Meldung ueber das **Meldeportal der BaFin**.

---

## ComplianceOS-Mapping

| DORA-Saeule | ComplianceOS-Domain | Hinweise |
|---|---|---|
| ICT-Risikomanagement | RISK + CONFIG | Schutzbedarfsfeststellung pro System |
| Incident-Reporting | INCIDENT | Klassifikations-Logik mit konfigurierbaren Schwellen |
| Resilience-Testing | BCP + VULN | TLPT-Vorbereitungs-Workflows |
| Drittparteien-Management | SUPPLY | Tagging fuer Critical-ICT-Provider |
| Informationsaustausch | LOGGING | strukturierte Threat-Intel-Importe |

DORA-Plugin importiert die RTS-Definitionen, sodass Findings direkt
nach DORA-Kriterien klassifiziert werden koennen.

---

## Verweise

- EU 2022/2554 (DORA): [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- TIBER-EU Framework: ECB
- BaFin DORA-Anwendungsleitfaden

ComplianceOS-Doku zum [Standards-Ueberblick](../../referenz/standards.md).
