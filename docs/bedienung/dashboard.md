# Dashboard

Das Dashboard ist die Startseite von ComplianceOS und zeigt den aktuellen Compliance-Status auf einen Blick.

![Dashboard Uebersicht](../screenshots/dashboard/dashboard-overview.png)

## Compliance-Score

Der zentrale Score-Ring zeigt den Gesamt-Compliance-Grad in Prozent. Die Farbe aendert sich je nach Ergebnis:

- **Gruen (80-100%):** Guter Compliance-Stand
- **Gelb (50-79%):** Verbesserungsbedarf
- **Rot (0-49%):** Dringender Handlungsbedarf

## Domain-Scores

Unterhalb des Score-Rings sehen Sie die Bewertung fuer jede der 12 Domains:

| Domain | Pruefbereich |
|--------|-------------|
| CRYPTO | Verschluesselung und Kryptografie |
| ACCESS | Zugriffskontrolle und Authentifizierung |
| BACKUP | Datensicherung und Wiederherstellung |
| LOGGING | Protokollierung und Monitoring |
| NETWORK | Netzwerksicherheit |
| INCIDENT | Incident Management |
| VULN | Schwachstellenmanagement |
| BCP | Business Continuity |
| SUPPLY | Lieferanten-Management |
| PII | Datenschutz (personenbezogene Daten) |
| CONFIG | Konfigurationsmanagement |
| MALWARE | Malware-Schutz |

## Findings-Zusammenfassung

Das Dashboard zeigt die Anzahl offener Findings nach Severity:

- **Major NC** — Schwerwiegende Nichtkonformitaeten
- **Minor NC** — Geringfuegige Nichtkonformitaeten
- **Observations** — Beobachtungen
- **OFI** — Verbesserungsmoeglichkeiten

## Letzte Audits

Eine Liste der juengsten Audit-Laeufe mit Datum, Modus und Ergebnis-Zusammenfassung.

!!! tip "Projekt wechseln"
    Oben rechts koennen Sie zwischen Projekten wechseln.
    Jedes Projekt hat eigene Audit-Ergebnisse und Findings.
