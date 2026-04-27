# Example: ISO 27001 Audit — Mid-Sized Enterprise

> **Hinweis:** Diese Walkthrough-Datei ist eine illustrative Modell-Rechnung,
> kein Vertragsgegenstand. Reale Werte haengen von Reifegrad, Asset-Komplexitaet
> und Integrationstiefe ab.

## Setup

- **Organisation:** Mittelstaendler, 500 Mitarbeiter, IT-Dienstleister
- **Pflicht-Standards:** ISO/IEC 27001:2022 (Erstzertifizierung)
- **Audit-Zyklus:** Stage 1 + Stage 2, danach jaehrliche Ueberwachungsaudits, Rezertifizierung alle 3 Jahre
- **Team:** 1 CISO, 2 Compliance-Teilzeitstellen (2,0 FTE)

## Audit-Aufwand klassisch (ohne Tool)

- Anzahl Annex-A-Controls: 93
- Vorbereitungszeit vor Stage 1: 90 Tage (Dokumenten-Sammeln, Findings-Tracking in Excel, Interview-Koordination)
- Interne FTE-Wochen pro Zyklus: 15
- Externer Auditor (akkreditiert): 10 Personentage Stage 1+2 (Tagessatz 2.000-3.000 EUR)
- Tool-Kosten: 0 (Excel-Sheets)

## Audit-Aufwand mit ComplianceOS

- Tool-Setup: 5 Tage (Asset-Inventar-Import, Standard-Aktivierung, ISMS-Mapping)
- Automatische Checks: 60 von 93 Annex-A-Controls automatisiert verifizierbar (techn. Kontrollen, Logging, Backup, Crypto)
- Manuelle Reviews: 33 organisatorische Controls (Policy, Awareness, Supplier-Management)
- Vorbereitungszeit vor Stage 1: 30 Tage mit iterativer Gap-Analyse
- Interne FTE-Wochen pro Zyklus: 5
- Externer Auditor: unveraendert 10 Personentage (Tool ersetzt keinen Auditor)

## Delta

| Metrik | Vorher | Nachher | Delta |
|---|---|---|---|
| Audit-Vorbereitungszeit | 90 Tage | 30 Tage | -60 Tage (-67 %) |
| Interne FTE-Wochen pro Zyklus | 15 | 5 | -10 FTE-Wochen |
| Findings-Tracking | Excel + Mail | Dashboard mit Drift-Detection | qualitativ |
| Evidence-Bereitstellung | manuell | semi-automatisch | qualitativ |

## Pilot-Umfang

- 90-Tage-Pilot mit ISO 27001 Annex A
- Begleitung durch silentspike (fachlich + tooltechnisch)
- Vollstaendige Audit-Artefakte fuer Stage-1-Vorbereitung am Ende des Pilots

## Caveats

- ROI ist illustrativ. Tatsaechliche Einsparung stark abhaengig von vorhandener Doku-Qualitaet.
- Externer Auditor-Aufwand bleibt — ComplianceOS ersetzt keinen akkreditierten Auditor.
- Erstzertifizierung erfordert hoeheren Aufwand als Ueberwachungsaudits.

## Verweise

- [ROI-Szenarien (Uebersicht)](../docs/business/roi.md)
- [Sample Audit Report](../docs/samples/sample-audit-report.html)
- [Evaluation Request Template](https://github.com/silentspike/complianceos/issues/new?template=evaluation_request.yml)
