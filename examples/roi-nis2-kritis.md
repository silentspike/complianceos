# Example: NIS2 / KritisV — KRITIS Operator

> **Hinweis:** Diese Walkthrough-Datei ist eine illustrative Modell-Rechnung,
> kein Vertragsgegenstand. Reale Werte haengen von Sektor (Energie/Wasser/
> Telekom), Anlagengroesse und vorhandener IT-Sicherheitsorganisation ab.

## Setup

- **Organisation:** Regionaler Energieversorger, 800 Mitarbeiter
- **Pflicht-Standards:** NIS2-Umsetzungsgesetz (BSIG §8a/§8b), KritisV, B3S Sektor-spezifisch, ISO 27001 (freiwillig als Nachweisrahmen)
- **Audit-Zyklus:** §8a-Nachweis alle 2 Jahre, Stoerfall-Meldung 24h-Frist, jaehrlicher Bericht ans BSI
- **Team:** 1 IT-Sicherheitsbeauftragter (ITSB), 1 OT-Security-Spezialist, externe Audit-Begleitung

## Audit-Aufwand klassisch (ohne Tool)

- §8a-Nachweis: 6-12 Monate Vorbereitung mit externem Auditor
- Maßnahmenkatalog NIS2 Art. 21: 10 Bereiche manuell dokumentieren (Risikomanagement, Incident-Handling, BCM, Supply-Chain, ...)
- Interne FTE-Wochen pro Nachweis-Zyklus: 25-30
- Externer Auditor: 12-15 Personentage
- Stoerfall-Dokumentation: ad hoc, manuelle Ticket-Trail-Aufbereitung
- Tool-Kosten: 0 (Excel + SharePoint)

## Audit-Aufwand mit ComplianceOS

- Tool-Setup: 7 Tage (NIS2-Maßnahmenkatalog laden, B3S-Sektor-Profil aktivieren, Asset-Inventar mit OT-Komponenten)
- Automatische Checks: 70 von 135 Controls automatisiert (Crypto, Logging, Patch-Status, Network-Segmentierung)
- Manuelle Reviews: 65 organisatorische und OT-spezifische Controls
- Stoerfall-Dokumentation: zentralisiert mit Findings-Tracking (24h-Meldung als Workflow)
- Interne FTE-Wochen pro Nachweis-Zyklus: 10-12
- Externer Auditor: unveraendert 12-15 Personentage

## Delta

| Metrik | Vorher | Nachher | Delta |
|---|---|---|---|
| Vorbereitung §8a-Nachweis | 6-12 Monate | 3-6 Monate | -50 % |
| Interne FTE-Wochen pro Zyklus | 25-30 | 10-12 | -55 % |
| Stoerfall-Doku-Latenz | ad hoc | live im Dashboard | qualitativ |
| Cross-Standard-Mapping (NIS2 ↔ B3S ↔ ISO 27001) | manuell | automatisch | qualitativ |

## Pilot-Umfang

- 90-Tage-Pilot mit NIS2-Maßnahmenkatalog Art. 21 + B3S-Sektor
- OT-Asset-Integration als optionaler Pilot-Baustein
- 24h-Stoerfall-Workflow als Demo-Setup

## Caveats

- KRITIS-Einstufung muss vorab geklaert sein (Schwellenwerte BSI-KritisV)
- OT-Komponenten-Discovery ist organisationsspezifisch (Tool-Default deckt IT, OT braucht individuellen Connector)
- Externer Auditor weiterhin Pflicht fuer §8a-Nachweis

## Verweise

- [NIS2 Detailseite](../docs/business/regulations/nis2.md)
- [B3S Krankenhaus + KHZG (analoges Sektor-Beispiel)](../docs/business/regulations/b3s-krankenhaus.md)
- [ROI-Szenarien (Uebersicht)](../docs/business/roi.md)
- [Evaluation Request Template](https://github.com/silentspike/complianceos/issues/new?template=evaluation_request.yml)
