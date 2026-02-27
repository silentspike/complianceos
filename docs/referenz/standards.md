# Standards

ComplianceOS unterstuetzt 9 internationale Sicherheits- und Compliance-Standards. Jeder Standard wird durch technische Controls in der Control-Matrix abgebildet und bei Audits geprueft.

---

## Uebersicht

| Standard | Version | Typ | Fokus | Controls |
|----------|---------|-----|-------|----------|
| ISO/IEC 27001 | 2022 | Zertifizierung | Informationssicherheits-Management (ISMS) | 36 |
| ISO 22301 | 2019 | Zertifizierung | Business Continuity Management | 12 |
| ISO/IEC 27005 | 2022 | Leitfaden | Risikomanagement fuer Informationssicherheit | 10 |
| ISO/IEC 27017 | 2015 | Leitfaden | Cloud-Sicherheit | 14 |
| ISO/IEC 27018 | 2019 | Leitfaden | Datenschutz in der Cloud (PII) | 8 |
| ISO/IEC 27035 | 2023 | Leitfaden | Incident Management | 11 |
| NIS2 | 2022/2555 | EU-Richtlinie | Netz- und Informationssicherheit | 18 |
| BSI IT-Grundschutz | 2023 | Framework | IT-Sicherheit (DACH-spezifisch) | 16 |
| DSGVO | 2016/679 | EU-Verordnung | Datenschutz | 10 |

**Gesamt:** 135 Controls, verteilt auf 12 Sicherheitsdomains, geprueft durch 2.042 AUDIT-CHECKs.

---

## ISO/IEC 27001:2022

Der internationale Standard fuer Informationssicherheits-Managementsysteme (ISMS). ISO 27001 ist der am weitesten verbreitete Sicherheitsstandard und bildet die Grundlage fuer viele andere Standards.

**ComplianceOS deckt ab:**

| Bereich | Inhalt | Controls |
|---------|--------|----------|
| **Clauses 4-10** | Anforderungen an das Managementsystem (Kontext, Fuehrung, Planung, Unterstuetzung, Betrieb, Bewertung, Verbesserung) | 7 |
| **Annex A** | 93 Controls in 4 Kategorien | 29 |

**Annex A Kategorien:**

- **Organisatorische Controls** (A.5): Policies, Rollen, Klassifikation
- **Personenbezogene Controls** (A.6): Screening, Schulung, Verantwortlichkeiten
- **Physische Controls** (A.7): Zutrittsschutz, Geraeteschutz
- **Technologische Controls** (A.8): Authentifizierung, Kryptografie, Netzwerk, Logging

**Domains:** ACCESS, BACKUP, CONFIG, CRYPTO, INCIDENT, LOGGING, MALWARE, NETWORK, SUPPLY, VULN

---

## ISO 22301:2019

Business Continuity Management (BCM). Stellt sicher dass Ihre Organisation auch bei Stoerungen handlungsfaehig bleibt.

**Pruefbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Business Impact Analyse (BIA)** | Identifikation kritischer Geschaeftsprozesse und deren Abhaengigkeiten |
| **RPO/RTO-Definitionen** | Recovery Point Objective und Recovery Time Objective fuer alle kritischen Systeme |
| **Notfallplaene** | Dokumentierte Reaktionsplaene fuer verschiedene Szenarien |
| **Notfalluebungen** | Regelmaessige Tests der Wiederanlaufverfahren |
| **Wiederanlauf** | Verfahren zur Wiederherstellung des Normalbetriebs |

**Domains:** BACKUP, BCP

---

## ISO/IEC 27005:2022

Risikomanagement fuer Informationssicherheit. Ergaenzt ISO 27001 um einen systematischen Risikomanagement-Prozess.

**Pruefbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Risiko-Identifikation** | Systematische Erfassung von Bedrohungen und Schwachstellen |
| **Risiko-Analyse** | Bewertung von Eintrittswahrscheinlichkeit und Auswirkung |
| **Risiko-Bewertung** | Priorisierung anhand der Risiko-Matrix |
| **Risiko-Behandlung** | Massnahmenplanung (Vermeiden, Reduzieren, Uebertragen, Akzeptieren) |
| **Risiko-Kommunikation** | Berichterstattung an Stakeholder |

**Domains:** Alle Domains (uebergreifend)

---

## ISO/IEC 27017:2015

Cloud-spezifische Sicherheitsanforderungen. Erweitert ISO 27001 um Controls die speziell fuer Cloud-Umgebungen relevant sind.

**Pruefbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Shared Responsibility** | Klare Abgrenzung der Verantwortlichkeiten zwischen Cloud-Provider und Cloud-Kunde |
| **Cloud-Service-Provider Controls** | Anforderungen an den Cloud-Anbieter |
| **Mandantentrennung** | Isolation zwischen verschiedenen Mandanten |
| **Virtualisierungs-Sicherheit** | Schutz der Virtualisierungsschicht |
| **Cloud-spezifische Verschluesselung** | Datenverschluesselung in Transit und at Rest |

**Domains:** CONFIG, CRYPTO, NETWORK, ACCESS

---

## ISO/IEC 27018:2019

Datenschutz in der Cloud — Schutz personenbezogener Daten (PII) bei Cloud-Services.

**Pruefbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **PII-Verarbeitung** | Rechtmaessige Verarbeitung personenbezogener Daten in der Cloud |
| **Transparenz** | Information der Betroffenen ueber Datenverarbeitung |
| **Einwilligung** | Nachweis der Einwilligung zur Datenverarbeitung |
| **Datenportabilitaet** | Moeglichkeit zum Export personenbezogener Daten |
| **Subunternehmer** | Kontrolle von Sub-Auftragsverarbeitern |

**Domains:** PII, ACCESS

---

## ISO/IEC 27035:2023

Incident Management — systematische Erkennung, Behandlung und Nachbereitung von Sicherheitsvorfaellen.

**Pruefbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Erkennung** | Mechanismen zur Erkennung von Sicherheitsvorfaellen |
| **Meldung** | Meldewege und Eskalationsstufen |
| **Klassifikation** | Bewertung und Einstufung der Severity |
| **Reaktion** | Eindaemmung, Beseitigung und Wiederherstellung |
| **Nachbereitung** | Lessons Learned und Prozessverbesserung |

**Domains:** INCIDENT, LOGGING

---

## NIS2 (EU 2022/2555)

Die EU-Richtlinie fuer Netz- und Informationssicherheit. Betrifft wesentliche und wichtige Einrichtungen in 18 Sektoren.

**Pruefbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Risikomanagement** | Technische und organisatorische Massnahmen |
| **Meldepflichten** | 24h Fruehwarnung, 72h Erstmeldung, Abschlussbericht |
| **Supply-Chain** | Sicherheit in der Lieferkette |
| **Business Continuity** | Notfall- und Wiederanlaufplaene |
| **Verschluesselung** | Kryptografie-Anforderungen |
| **Schulung** | Cyber-Hygiene und Awareness fuer Fuehrungskraefte |

**Domains:** CRYPTO, ACCESS, BACKUP, INCIDENT, NETWORK, SUPPLY, BCP

!!! warning "NIS2-Umsetzungsfrist"
    Die nationale Umsetzung der NIS2-Richtlinie muss bis Oktober 2024 erfolgen. Pruefen Sie ob Ihre Organisation betroffen ist.

---

## BSI IT-Grundschutz

Das deutsche Framework fuer IT-Sicherheit vom Bundesamt fuer Sicherheit in der Informationstechnik.

**Absicherungsniveaus:**

| Niveau | Beschreibung |
|--------|-------------|
| **Basis-Absicherung** | Grundlegende Schutzmassnahmen fuer alle Systeme |
| **Standard-Absicherung** | Vollstaendige Umsetzung der IT-Grundschutz-Bausteine |
| **Kern-Absicherung** | Erhoehter Schutz fuer besonders kritische Systeme |

ComplianceOS prueft gegen die relevanten **IT-Grundschutz-Bausteine** aus dem Kompendium.

**Domains:** CONFIG, MALWARE, NETWORK, LOGGING, VULN

---

## DSGVO (EU 2016/679)

Datenschutz-Grundverordnung — EU-weite Regelung zum Schutz personenbezogener Daten.

**Pruefbereiche:**

| Bereich | Beschreibung |
|---------|-------------|
| **Verarbeitungsverzeichnis** | Dokumentation aller Verarbeitungstaetigkeiten (Art. 30) |
| **TOMs** | Technische und organisatorische Massnahmen (Art. 32) |
| **DSFA** | Datenschutz-Folgenabschaetzung bei hohem Risiko (Art. 35) |
| **Betroffenenrechte** | Auskunft, Loeschung, Berichtigung, Portabilitaet (Art. 15-22) |
| **Auftragsverarbeitung** | Vertraege mit Auftragsverarbeitern (Art. 28) |
| **Meldepflichten** | Meldung von Datenschutzverletzungen (Art. 33/34) |

**Domains:** PII, ACCESS, LOGGING

!!! info "DSGVO aktivieren"
    Die DSGVO-Pruefung kann ueber das Feature-Flag `ENABLE_DSGVO=true` in den Einstellungen aktiviert oder deaktiviert werden.

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
    Fuer eine interaktive Visualisierung der Standard-Ueberschneidungen nutzen Sie die [Cross-Standard-Analyse](../bedienung/reports.md) unter Reports.
