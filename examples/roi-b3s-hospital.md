# Example: B3S-Krankenhaus + DSGVO — Hospital Compliance

> **Hinweis:** Diese Walkthrough-Datei ist eine illustrative Modell-Rechnung,
> kein Vertragsgegenstand. Reale Werte haengen von Klinik-Groesse, KIS-Setup
> und vorhandener IT-Sicherheits-Reife ab.

## Setup

- **Organisation:** Krankenhaus mit 600 Betten, 1.500 Mitarbeiter
- **Pflicht-Standards:** B3S Branchenspezifischer Sicherheitsstandard Krankenhaus, DSGVO (Patientendaten), KHZG-Foerderungstatbestand 10 (IT-Sicherheit), NIS2 (Krankenhaeuser ab 30k Vollstationaer)
- **Audit-Zyklus:** §8a-Nachweis alle 2 Jahre, MDR-Audit fuer Medizingeraete jaehrlich, DSGVO-Audit auf Beschwerdebasis
- **Team:** 1 ITSB, 1 Datenschutzbeauftragter (DSB), externe Beratung

## Audit-Aufwand klassisch (ohne Tool)

- B3S-Anforderungskatalog: 168 Anforderungen ueber 13 Themenbereiche
- Vorbereitungszeit: 4-6 Monate mit externem Auditor
- Interne FTE-Wochen pro Zyklus: 20-25
- Externer Auditor: 10-12 Personentage
- DSGVO-Doku: separates Verzeichnis von Verarbeitungstaetigkeiten (VVT) in SharePoint
- KHZG-Nachweis: zusaetzliche 4 Wochen Aufbereitung des Foerdermittelnachweises

## Audit-Aufwand mit ComplianceOS

- Tool-Setup: 7 Tage (B3S-Profil + DSGVO-Modul + KHZG-Mapping)
- Automatische Checks: 80 von 168 B3S-Anforderungen technisch verifizierbar (Backup, Crypto, Patch-Status, Logging, Netzwerk-Segmentierung)
- Manuelle Reviews: 88 organisatorische und prozessuale Anforderungen
- DSGVO-VVT: integriert mit B3S-Asset-Inventar (Kreuzverweise automatisch)
- KHZG-Nachweis: aus Audit-Lauf direkt exportierbar
- Interne FTE-Wochen pro Zyklus: 8-10
- Externer Auditor: unveraendert 10-12 Personentage

## Delta

| Metrik | Vorher | Nachher | Delta |
|---|---|---|---|
| Vorbereitung B3S-Nachweis | 4-6 Monate | 2-3 Monate | -50 % |
| Interne FTE-Wochen pro Zyklus | 20-25 | 8-10 | -60 % |
| DSGVO-VVT-Pflege | quartaerlich manuell | live mit B3S-Asset-Inventar gekoppelt | qualitativ |
| KHZG-Nachweis-Aufbereitung | 4 Wochen | aus Audit-Lauf exportierbar | -3+ Wochen |

## Pilot-Umfang

- 90-Tage-Pilot mit B3S-Krankenhaus-Profil + DSGVO-Modul
- KHZG-Reporting-Integration als optionaler Pilot-Baustein
- Schulung von ITSB + DSB im Tool

## Caveats

- KHZG-Foerderung-Anerkennung haengt vom Bundesland und der konkreten Foerdermittel-Verwendung ab
- B3S-Auditor-Akkreditierung ist sektorspezifisch (BSI-Liste konsultieren)
- Patientendaten verlassen die Klinik nie (siehe [AI Deployment in regulierten Umgebungen](../docs/business/ai-deployment-relevance.md))

## Verweise

- [B3S Krankenhaus + KHZG Detailseite](../docs/business/regulations/b3s-krankenhaus.md)
- [AI Deployment in regulierten Umgebungen](../docs/business/ai-deployment-relevance.md)
- [ROI-Szenarien (Uebersicht)](../docs/business/roi.md)
- [Evaluation Request Template](https://github.com/silentspike/complianceos/issues/new?template=evaluation_request.yml)
