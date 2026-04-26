# BSI IT-Grundschutz

> **Kontext:** Der BSI IT-Grundschutz ist die in Deutschland etablierte
> Methodik zur ganzheitlichen Informationssicherheit fuer den oeffentlichen
> Sektor und Betreiber kritischer Infrastrukturen. Das aktuelle BSI
> IT-Grundschutz-Kompendium 2023 enthaelt etwa 100 Bausteine in 10
> Schichten und setzt auf Kombination mit ISO 27001 (Basis-Absicherung,
> Standard-Absicherung, Kern-Absicherung).

---

## Methodik

Der IT-Grundschutz folgt einer dreistufigen Vorgehensweise:

1. **Strukturanalyse** — Ermittlung des Informationsverbunds (Systeme,
   Anwendungen, Standorte, Personal, Geschaeftsprozesse)
2. **Schutzbedarfsfeststellung** — Klassifikation der Werte in **normal**,
   **hoch** und **sehr hoch** je Schutzziel (Vertraulichkeit, Integritaet,
   Verfuegbarkeit)
3. **Modellierung** — Zuordnung von Bausteinen aus dem Kompendium zu
   den Komponenten des Informationsverbunds

---

## Drei Vorgehensweisen

| Variante | Zielgruppe | Aufwand |
|---|---|---|
| **Basis-Absicherung** | KMU oder erste ISMS-Stufe | gering — verbindliche Basis-Anforderungen |
| **Kern-Absicherung** | Fokus auf besonders kritische Werte | mittel — Konzentration auf Kronjuwelen |
| **Standard-Absicherung** | Vollausbau, Ziel ISO-27001-Zertifizierung auf Basis IT-Grundschutz | hoch — vollstaendige Modellierung |

Die Standard-Absicherung gilt als Vorlaeufer fuer eine ISO-27001-
Zertifizierung auf Basis IT-Grundschutz, die in der oeffentlichen
Verwaltung breit eingesetzt wird.

---

## Baustein-Schichten

Das Kompendium organisiert Bausteine in zehn Schichten — jeweils mit
prozessualer und technischer Auspraegung:

| Schicht | Beispiel-Bausteine |
|---|---|
| ISMS | Sicherheitsmanagement |
| ORP | Personal, Organisation |
| CON | Kryptokonzept, Datensicherung |
| OPS | Patch-Management, Schwachstellenmanagement |
| DER | Detektion + Reaktion |
| APP | Webanwendungen, Office-Produkte |
| SYS | Allgemeiner Server, Windows-Client |
| IND | ICS-Komponenten, ICS-Netze |
| NET | Firewall, WLAN |
| INF | Allgemeines Gebaeude, Rechenzentrum |

Jeder Baustein definiert Basis-Anforderungen (verbindlich), Standard-
Anforderungen und Anforderungen bei erhoehtem Schutzbedarf.

---

## Schutzbedarfs-Mapping

Schutzbedarf wird kompakt in einer Schutzbedarfsfeststellung
dokumentiert. Beispiel-Klassifikation:

| Schutzziel | normal | hoch | sehr hoch |
|---|---|---|---|
| Vertraulichkeit | oeffentlich verfuegbare Daten | personenbezogene Daten | Staatsgeheimnisse, Patientendaten Art. 9 |
| Integritaet | redaktionelle Drucksachen | Buchhaltungsdaten | Steuerungsdaten Notfallinfrastruktur |
| Verfuegbarkeit | Toleranz Tage | Toleranz Stunden | Toleranz Minuten |

Das Schutzbedarfs-Mapping vererbt sich entlang Abhaengigkeiten — eine
Anwendung mit hohem Schutzbedarf zwingt typischerweise die unterliegende
Datenbank in den gleichen Schutzbedarf.

---

## Pruefer und Nachweise

| Aspekt | Detail |
|---|---|
| Pruefer | BSI-zertifizierte IT-Grundschutz-Auditoren |
| Zertifizierung | ISO 27001 auf Basis IT-Grundschutz (Pruefverfahrenskompetenz beim BSI) |
| Pruefzyklus | 3 Jahre Hauptaudit + jaehrliche Ueberwachungsaudits |
| Nachweis | Referenzdokumente A.0 bis A.6 (Sicherheitskonzept, Realisierungsplan, etc.) |

---

## ComplianceOS-Mapping

| Methodik-Schritt | ComplianceOS-Funktion |
|---|---|
| Strukturanalyse | Asset-Inventory mit Tagging fuer Bausteine |
| Schutzbedarfsfeststellung | pro Asset konfigurierbar (CIA-Triade x normal/hoch/sehr hoch) |
| Modellierung | Bausteine als Standard-Plugin, Zuordnung Asset → Bausteine |
| Pruefung | Findings pro Anforderung mit Verbindlichkeitsstufe |
| Reporting | BSI-Report-Format A.0–A.6, Drift-Detection zwischen Audits |

Cross-Standard-Mapping zeigt die Kongruenz zwischen IT-Grundschutz-
Bausteinen und ISO 27001 Annex A — was die Doppelfuehrung in
Behoerden mit ISO + IT-Grundschutz vereinfacht.

---

## Verweise

- BSI IT-Grundschutz-Kompendium 2023: [bsi.bund.de](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html)
- BSI Mindeststandards fuer IT des Bundes
- ISO/IEC 27001:2022

ComplianceOS-Doku zum [Standards-Ueberblick](../../referenz/standards.md).
