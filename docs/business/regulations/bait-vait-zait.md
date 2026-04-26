# BAIT / VAIT / ZAIT (BaFin)

> **Kontext:** Die Bankaufsichtlichen Anforderungen an die IT (BAIT), die
> Versicherungsaufsichtlichen Anforderungen an die IT (VAIT) und die
> Zahlungsdiensteaufsichtlichen Anforderungen an die IT (ZAIT) sind drei
> aufsichtliche Verlautbarungen der BaFin, die die regulatorischen
> Erwartungen an die IT-Organisation finanzdienstleistender Unternehmen
> konkretisieren. Sie sind eng verwandt — unterscheiden sich aber im
> Geltungsbereich und in einzelnen sektoralen Spezifika.

---

## Abgrenzung der drei Rundschreiben

| Verlautbarung | Adressaten | Aufsicht |
|---|---|---|
| **BAIT** | Kreditinstitute, Finanzdienstleistungsinstitute (KWG) | BaFin |
| **VAIT** | Erst- und Rueckversicherungsunternehmen, Pensionskassen, Versicherungs-Holdings | BaFin |
| **ZAIT** | Zahlungsinstitute, E-Geld-Institute (ZAG) | BaFin |

Wer in mehreren Sektoren taetig ist (z.B. Bank mit Versicherungs-
Tochter), erfuellt parallel die jeweils anwendbaren Vorgaben — hier zahlt
sich Cross-Mapping aus.

---

## Gemeinsame Themenfelder

Alle drei Verlautbarungen folgen demselben Aufbau und decken acht bis
zehn Themenfelder ab, darunter:

- IT-Strategie + IT-Governance
- Informations-Risikomanagement (Schutzbedarfsfeststellung, Risikoanalyse)
- Informationssicherheits-Management
- Operativer Informationssicherheits-Betrieb (Vulnerability-Management,
  Patch-Management)
- Identitaets- und Rechte-Management (kritische Privilegien)
- IT-Projekte + Anwendungsentwicklung (Change-Management)
- IT-Betrieb (Datensicherung, Verfuegbarkeitsmanagement)
- Auslagerungen + sonstige Fremdbezuege (eng mit DORA verzahnt)
- Kritische Infrastrukturen (sektorenspezifisch)

---

## Pruefer und Pruefzyklen

| Aspekt | Detail |
|---|---|
| Interne Revision | jaehrliches Pruefprogramm mit BAIT/VAIT/ZAIT-Schwerpunkten |
| Externe Wirtschaftspruefer | jaehrliche Jahresabschlusspruefung mit IT-Pruefungs-Anteilen |
| BaFin-Sonderpruefungen | nach Anlass (Vorfaelle, Hinweise, Schwerpunktpruefungen) |
| Berichtsweg | Pruefberichte an Aufsichtsorgane + BaFin |

---

## Verzahnung mit DORA

Mit Anwendung von **DORA** (EU 2022/2554, Anwendung ab 17. Januar 2025)
werden zentrale Themen aus BAIT/VAIT/ZAIT auf EU-Ebene harmonisiert:

- Auslagerungs- und Drittparteien-Management
- Incident-Klassifikation und Meldung
- Threat-Led-Penetration-Testing (TLPT)
- ICT-Risikomanagement-Framework

BAIT/VAIT/ZAIT bleiben fuer nationale Spezifika und Aufsichts-Erwartungen
relevant; DORA setzt die EU-weite Mindestlinie. ComplianceOS modelliert
beide Ebenen (siehe auch [DORA-Detailseite](dora.md)).

---

## ComplianceOS-Mapping

| Themenfeld | ComplianceOS-Domain |
|---|---|
| Informations-Risikomanagement | RISK + CONFIG |
| Informationssicherheits-Management | ACCESS + LOGGING |
| Vulnerability + Patch-Management | VULN |
| Identity + Access | ACCESS (12 Controls) |
| Change-Management + Entwicklung | CONFIG |
| Datensicherung + Verfuegbarkeit | BACKUP + BCP |
| Auslagerungen + Drittparteien | SUPPLY |
| Kryptografie | CRYPTO |
| Incident-Klassifikation | INCIDENT |

Standard-Plugins fuer BAIT, VAIT, ZAIT laden den jeweiligen Pflicht-Set
und erzeugen aufsichtskonforme Reports — die Findings-Datenbank ist eine,
die Pruefberichts-Sicht waehlbar.

---

## Verweise

- BAFIN — Bankaufsichtliche Anforderungen an die IT (BAIT): [bafin.de](https://www.bafin.de/SharedDocs/Veroeffentlichungen/DE/Rundschreiben/2017/rs_1710_ba_BAIT.html)
- BAFIN — Versicherungsaufsichtliche Anforderungen an die IT (VAIT)
- BAFIN — Zahlungsdiensteaufsichtliche Anforderungen an die IT (ZAIT)
- DORA: [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)

ComplianceOS-Doku zum [Standards-Ueberblick](../../referenz/standards.md).
