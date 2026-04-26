# B3S Krankenhaus + KHZG

> **Kontext:** Der branchenspezifische Sicherheitsstandard B3S Krankenhaus
> ist von der Deutschen Krankenhausgesellschaft (DKG) erarbeitet und vom
> BSI anerkannt. Er konkretisiert die KRITIS-Anforderungen fuer
> Versorgungs-Krankenhaeuser ab 30.000 vollstationaeren Faellen pro Jahr.
> Mit dem Krankenhauszukunftsgesetz (KHZG) wurde IT-Sicherheit zudem an
> Foerdertatbestaende gekoppelt.

---

## Geltungsbereich

- **B3S Krankenhaus**: Pflichtanwendung fuer KRITIS-Krankenhaeuser ab
  30.000 vollstationaeren Faellen jaehrlich (KritisV).
- **KHZG**: Foerderprogramm fuer Krankenhaeuser, mehrere Foerdertatbestaende
  haben IT-Sicherheits-Bezug (insbesondere Foerdertatbestand 10 — IT-
  Sicherheit, plus implizit Tatbestaende 1 / 5 mit IT-Schutzbedarf).
- **DSGVO Art. 9** (besonders schuetzenswerte Daten — Gesundheitsdaten)
  greift unabhaengig von der KRITIS-Schwelle.

---

## Pruefzyklus und Pruefer

| Aspekt | Detail |
|---|---|
| Pruefzyklus | alle 2 Jahre |
| Pruefende Stelle | nach BSI-Anforderungen anerkannte Pruefer |
| Berichtsweg | Pruefbericht an BSI |
| Sanktion bei Verstoessen | Bussgelder nach BSI-Gesetz, Reputations-Folgen |

---

## Schutzziele und Anforderungs-Bereiche

Der B3S strukturiert Anforderungen entlang sechs Bereichen, die jeweils
mit konkreten Massnahmen-Anforderungen hinterlegt sind:

1. **Organisation der Informationssicherheit** — ISMS, Rollen, Verantwortlichkeiten
2. **Personalsicherheit** — Schulung, Awareness, Geheimhaltung
3. **Asset-Management** — Inventarisierung, Klassifizierung
4. **Zugriffskontrolle** — RBAC, Notfall-Zugriff mit Audit-Trail
5. **Kryptografie + Datentraegerverwaltung**
6. **Physische Sicherheit + Betriebssicherheit** — inkl. Medizingeraete-
   Netzsegmentierung

Praxis-Schwerpunkte sind Notfall-Zugriff (Patientensicherheit ueber
Datenschutz) und Medizingeraete-Vernetzung (IEC 80001-1).

---

## KHZG-Foerdertatbestaende mit IT-Sicherheits-Bezug

| Tatbestand | Inhalt | IT-Sicherheits-Beruehrung |
|---|---|---|
| FT 1 | Notfallkapazitaeten + Krankenhaus-Alarm- und Einsatzplanung | indirekt: kritische Systeme verfuegbar halten |
| FT 5 | Patienten-Portal | DSGVO-konforme Authentifizierung, Datenschutz |
| FT 10 | IT-Sicherheit (Hardware/Software, Schwachstellenmanagement, Awareness) | direkt — Hauptfoerderlinie fuer ISMS-Aufbau |

KHZG-Nachweise verlangen typischerweise eine Zuordnung der umgesetzten
Massnahme zum jeweiligen Foerdertatbestand.

---

## ComplianceOS-Mapping

ComplianceOS bildet B3S als eigene Standard-Auspraegung mit Cross-Mapping
zu ISO 27001 und DSGVO ab. Praktisch hilfreich:

- **Cross-Standard-Mapping** zeigt fuer jeden Control welche Standards
  ihn referenzieren — eine Massnahme deckt B3S, ISO und DSGVO gleichzeitig
- **Tagging-System** erlaubt Zuordnung zu KHZG-Foerdertatbestaenden, sodass
  der gleiche Findings-Bestand nachweisseitig pro Tatbestand gefiltert
  werden kann
- **Audit-Trail** dokumentiert Notfall-Zugriffe und Aenderungen an
  Zugriffsrechten
- **Network-Segmentation-Domain** fuer Medizingeraete-Zonen
- **PII-Domain (DSGVO Art. 9)** mit Betroffenen-Rechten-Checks

---

## Verweise

- DKG B3S-Krankenhaus (BSI-anerkannt): [bsi.bund.de](https://www.bsi.bund.de/DE/Themen/KRITIS-und-regulierte-Unternehmen/B3S-und-Pruefverfahrenskompetenz/B3S/b3s_node.html)
- KHZG (Krankenhauszukunftsgesetz): Bundesgesundheitsministerium
- IEC 80001-1: Risikomanagement fuer IT-Netzwerke mit Medizingeraeten
- DSGVO Art. 9: Verarbeitung besonderer Kategorien personenbezogener Daten

ComplianceOS-Doku zum [Standards-Ueberblick](../../referenz/standards.md).
