# Standards

ComplianceOS unterstützt 9 internationale Sicherheits- und Compliance-Standards. Jeder Standard wird durch technische Controls in der Control-Matrix abgebildet und bei Audits geprüft.

---

## Übersicht

| Standard | Version | Typ | Fokus | Controls |
|----------|---------|-----|-------|----------|
| ISO/IEC 27001 | 2022 | Zertifizierung | Informationssicherheits-Management (ISMS) | 36 |
| ISO 22301 | 2019 | Zertifizierung | Business Continuity Management | 12 |
| ISO/IEC 27005 | 2022 | Leitfaden | Risikomanagement für Informationssicherheit | 10 |
| ISO/IEC 27017 | 2015 | Leitfaden | Cloud-Sicherheit | 14 |
| ISO/IEC 27018 | 2019 | Leitfaden | Datenschutz in der Cloud (PII) | 8 |
| ISO/IEC 27035 | 2023 | Leitfaden | Incident Management | 11 |
| NIS2 | 2022/2555 | EU-Richtlinie | Netz- und Informationssicherheit | 18 |
| BSI IT-Grundschutz | 2023 | Framework | IT-Sicherheit (DACH-spezifisch) | 16 |
| DSGVO | 2016/679 | EU-Verordnung | Datenschutz | 10 |

**Gesamt:** 135 Controls, verteilt auf 12 Sicherheitsdomains, geprüft durch 2.042 AUDIT-CHECKs.

---

## ISO/IEC 27001:2022

Der internationale Standard für Informationssicherheits-Managementsysteme (ISMS). ISO 27001 ist der am weitesten verbreitete Sicherheitsstandard und bildet die Grundlage für viele andere Standards.

**ComplianceOS deckt ab:**

| Bereich | Inhalt | Controls |
|---------|--------|----------|
| **Clauses 4-10** | Anforderungen an das Managementsystem (Kontext, Führung, Planung, Unterstützung, Betrieb, Bewertung, Verbesserung) | 7 |
| **Annex A** | 93 Controls in 4 Kategorien | 29 |

**Annex A Kategorien:**

- **Organisatorische Controls** (A.5): Policies, Rollen, Klassifikation
- **Personenbezogene Controls** (A.6): Screening, Schulung, Verantwortlichkeiten
- **Physische Controls** (A.7): Zutrittsschutz, Geräteschutz
- **Technologische Controls** (A.8): Authentifizierung, Kryptografie, Netzwerk, Logging

**Domains:** ACCESS, BACKUP, CONFIG, CRYPTO, INCIDENT, LOGGING, MALWARE, NETWORK, SUPPLY, VULN

---

## ISO 22301:2019

Business Continuity Management (BCM). Stellt sicher dass Ihre Organisation auch bei Störungen handlungsfähig bleibt.

**Prüfbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Business Impact Analyse (BIA)** | Identifikation kritischer Geschäftsprozesse und deren Abhängigkeiten |
| **RPO/RTO-Definitionen** | Recovery Point Objective und Recovery Time Objective für alle kritischen Systeme |
| **Notfallpläne** | Dokumentierte Reaktionspläne für verschiedene Szenarien |
| **Notfallübungen** | Regelmässige Tests der Wiederanlaufverfahren |
| **Wiederanlauf** | Verfahren zur Wiederherstellung des Normalbetriebs |

**Domains:** BACKUP, BCP

---

## ISO/IEC 27005:2022

Risikomanagement für Informationssicherheit. Ergänzt ISO 27001 um einen systematischen Risikomanagement-Prozess.

**Prüfbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Risiko-Identifikation** | Systematische Erfassung von Bedrohungen und Schwachstellen |
| **Risiko-Analyse** | Bewertung von Eintrittswahrscheinlichkeit und Auswirkung |
| **Risiko-Bewertung** | Priorisierung anhand der Risiko-Matrix |
| **Risiko-Behandlung** | Massnahmenplanung (Vermeiden, Reduzieren, Übertragen, Akzeptieren) |
| **Risiko-Kommunikation** | Berichterstattung an Stakeholder |

**Domains:** Alle Domains (übergreifend)

---

## ISO/IEC 27017:2015

Cloud-spezifische Sicherheitsanforderungen. Erweitert ISO 27001 um Controls die speziell für Cloud-Umgebungen relevant sind.

**Prüfbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Shared Responsibility** | Klare Abgrenzung der Verantwortlichkeiten zwischen Cloud-Provider und Cloud-Kunde |
| **Cloud-Service-Provider Controls** | Anforderungen an den Cloud-Anbieter |
| **Mandantentrennung** | Isolation zwischen verschiedenen Mandanten |
| **Virtualisierungs-Sicherheit** | Schutz der Virtualisierungsschicht |
| **Cloud-spezifische Verschlüsselung** | Datenverschlüsselung in Transit und at Rest |

**Domains:** CONFIG, CRYPTO, NETWORK, ACCESS

---

## ISO/IEC 27018:2019

Datenschutz in der Cloud — Schutz personenbezogener Daten (PII) bei Cloud-Services.

**Prüfbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **PII-Verarbeitung** | Rechtmässige Verarbeitung personenbezogener Daten in der Cloud |
| **Transparenz** | Information der Betroffenen über Datenverarbeitung |
| **Einwilligung** | Nachweis der Einwilligung zur Datenverarbeitung |
| **Datenportabilität** | Möglichkeit zum Export personenbezogener Daten |
| **Subunternehmer** | Kontrolle von Sub-Auftragsverarbeitern |

**Domains:** PII, ACCESS

---

## ISO/IEC 27035:2023

Incident Management — systematische Erkennung, Behandlung und Nachbereitung von Sicherheitsvorfällen.

**Prüfbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Erkennung** | Mechanismen zur Erkennung von Sicherheitsvorfällen |
| **Meldung** | Meldewege und Eskalationsstufen |
| **Klassifikation** | Bewertung und Einstufung der Severity |
| **Reaktion** | Eindämmung, Beseitigung und Wiederherstellung |
| **Nachbereitung** | Lessons Learned und Prozessverbesserung |

**Domains:** INCIDENT, LOGGING

---

## NIS2 (EU 2022/2555)

Die EU-Richtlinie für Netz- und Informationssicherheit. Betrifft wesentliche und wichtige Einrichtungen in 18 Sektoren.

**Prüfbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Risikomanagement** | Technische und organisatorische Massnahmen |
| **Meldepflichten** | 24h Frühwarnung, 72h Erstmeldung, Abschlussbericht |
| **Supply-Chain** | Sicherheit in der Lieferkette |
| **Business Continuity** | Notfall- und Wiederanlaufpläne |
| **Verschlüsselung** | Kryptografie-Anforderungen |
| **Schulung** | Cyber-Hygiene und Awareness für Führungskräfte |

**Domains:** CRYPTO, ACCESS, BACKUP, INCIDENT, NETWORK, SUPPLY, BCP

!!! warning "NIS2-Umsetzungsfrist"
    Die nationale Umsetzung der NIS2-Richtlinie muss bis Oktober 2024 erfolgen. Prüfen Sie ob Ihre Organisation betroffen ist.

---

## BSI IT-Grundschutz

Das deutsche Framework für IT-Sicherheit vom Bundesamt für Sicherheit in der Informationstechnik.

**Absicherungsniveaus:**

| Niveau | Beschreibung |
|--------|-------------|
| **Basis-Absicherung** | Grundlegende Schutzmassnahmen für alle Systeme |
| **Standard-Absicherung** | Vollständige Umsetzung der IT-Grundschutz-Bausteine |
| **Kern-Absicherung** | Erhöhter Schutz für besonders kritische Systeme |

ComplianceOS prüft gegen die relevanten **IT-Grundschutz-Bausteine** aus dem Kompendium.

**Domains:** CONFIG, MALWARE, NETWORK, LOGGING, VULN

---

## DSGVO (EU 2016/679)

Datenschutz-Grundverordnung — EU-weite Regelung zum Schutz personenbezogener Daten.

**Prüfbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Verarbeitungsverzeichnis** | Dokumentation aller Verarbeitungstätigkeiten (Art. 30) |
| **TOMs** | Technische und organisatorische Massnahmen (Art. 32) |
| **DSFA** | Datenschutz-Folgenabschätzung bei hohem Risiko (Art. 35) |
| **Betroffenenrechte** | Auskunft, Löschung, Berichtigung, Portabilität (Art. 15-22) |
| **Auftragsverarbeitung** | Verträge mit Auftragsverarbeitern (Art. 28) |
| **Meldepflichten** | Meldung von Datenschutzverletzungen (Art. 33/34) |

**Domains:** PII, ACCESS, LOGGING

!!! info "DSGVO aktivieren"
    Die DSGVO-Prüfung kann über das Feature-Flag `ENABLE_DSGVO=true` in den Einstellungen aktiviert oder deaktiviert werden.

---

## Control-Verteilung nach Domain

| Domain | ISO 27001 | ISO 22301 | ISO 27005 | ISO 27017 | ISO 27018 | ISO 27035 | NIS2 | BSI | DSGVO | Gesamt |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|------|-----|-------|--------|
| ACCESS | 6 | - | 1 | 2 | 2 | - | 2 | 1 | 1 | 15 |
| BACKUP | 3 | 4 | - | - | - | - | 2 | - | 1 | 10 |
| BCP | 1 | 5 | - | - | - | - | 2 | - | - | 8 |
| CONFIG | 3 | - | - | 3 | - | - | 2 | 3 | 1 | 12 |
| CRYPTO | 4 | - | 1 | 3 | 1 | - | 3 | 1 | 1 | 14 |
| INCIDENT | 2 | 1 | 1 | - | - | 5 | 1 | - | 1 | 11 |
| LOGGING | 3 | - | 1 | 2 | 1 | 2 | 1 | 2 | - | 12 |
| MALWARE | 2 | - | - | - | - | - | 1 | 3 | 2 | 8 |
| NETWORK | 3 | - | 1 | 2 | 1 | 1 | 2 | 3 | - | 13 |
| PII | 2 | - | 1 | - | 3 | - | - | - | 4 | 10 |
| SUPPLY | 3 | 1 | 1 | - | - | 1 | 2 | - | - | 8 |
| VULN | 4 | 1 | 3 | 2 | - | 2 | - | 3 | - | 14 |

!!! tip "Cross-Standard-Mapping"
    Für eine interaktive Visualisierung der Standard-Überschneidungen nutzen Sie die [Cross-Standard-Analyse](../bedienung/reports.md) unter Reports.
