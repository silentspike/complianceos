# Fuer wen ist ComplianceOS?

ComplianceOS wurde fuer regulierte Organisationen und den oeffentlichen Sektor
entwickelt — dort wo Compliance nicht verhandelbar ist und Audit-Daten nicht
in eine fremde Cloud duerfen.

Die Plattform laeuft vollstaendig **on-premise**, versendet keinerlei
Telemetrie und ist bewusst proprietaer (EULA), damit Organisationen volle
Kontrolle ueber ihren Audit-Datenfluss behalten.

---

## 1. KRITIS-Betreiber (Energie, Wasser, Telekommunikation)

**Primaere Regulierungen:**

- NIS2 (EU-Richtlinie 2022/2555)
- BSI KRITIS-Verordnung (KritisV)
- BSI IT-Sicherheitsgesetz 2.0

**Typische Anforderungen:**

- Meldepflicht bei Sicherheitsvorfaellen (24h Erstmeldung, 72h Nachmeldung)
- Nachweis eines Informationssicherheits-Managementsystems (ISMS)
- Audits durch qualifizierte Pruefstellen im 2-Jahres-Rhythmus
- Business-Continuity-Plaene mit RPO/RTO-Nachweis

**Wie ComplianceOS unterstuetzt:**

- Vorkonfigurierte Control-Sets fuer NIS2-Annex und BSI-Bausteine
- Finding-Export im Format der BSI-Meldewege
- Drift-Detection zwischen Audit-Zyklen
- Incident-Response-Playbooks (ISO 27035)

---

## 2. Krankenhaeuser und Gesundheitsdienstleister

**Primaere Regulierungen:**

- B3S Krankenhaus (Branchenspezifischer Sicherheitsstandard)
- DSGVO (fuer Patientendaten)
- KHZG-relevante IT-Sicherheits-Foerdertatbestaende
- ISO 27001 / 27799 (Medizinische Informatik)

**Typische Anforderungen:**

- Patientendaten-Schutz mit Audit-Trail
- Nachweisbare Zugriffs-Kontrolle fuer Behandlerteams
- Notfall-Zugriff mit Dokumentation
- Medizingeraete-Netzsegmentierung

**Wie ComplianceOS unterstuetzt:**

- DSGVO-Standard-Plugin mit Betroffenen-Rechten-Checks
- Access-Control-Domain (12 Controls) fuer RBAC-Audits
- Network-Segmentation-Controls fuer Medizingeraete-Zonen

---

## 3. Finanzdienstleister (Banken, Versicherer, FinTechs)

**Primaere Regulierungen:**

- **BAIT** (Bankaufsichtliche Anforderungen an die IT, BaFin)
- **VAIT** (Versicherungsaufsichtliche Anforderungen an die IT)
- **ZAIT** (Zahlungsdiensteaufsichtliche Anforderungen)
- **DORA** (EU 2022/2554, Digital Operational Resilience Act)
- PCI DSS (Karten-Akzeptanz)

**Typische Anforderungen:**

- IKT-Risikomanagement-Framework
- Third-Party-Risk-Management mit kritischen Dienstleister-Registern
- Resilience-Testing (DORA TLPT)
- Incident-Classification + Reporting an BaFin

**Wie ComplianceOS unterstuetzt:**

- BCP-Domain (Business Continuity) mit RPO/RTO-Tracking
- Supply-Chain-Domain fuer Third-Party-Risk
- Incident-Domain mit konfigurierbaren Severity-Schwellwerten

---

## 4. Ministerien und oeffentliche Verwaltung

**Primaere Regulierungen:**

- **BSI IT-Grundschutz** (Kompendium 2023)
- BSI Mindeststandards fuer IT des Bundes
- IT-Sicherheitsgesetz 2.0
- Informationsfreiheitsgesetz-Implikationen

**Typische Anforderungen:**

- Schutzbedarfsfeststellung (normal, hoch, sehr hoch)
- Modellierung nach IT-Grundschutz-Bausteinen
- Basis-Absicherung plus Standard-Absicherung
- Jaehrliche ISB-Berichte

**Wie ComplianceOS unterstuetzt:**

- Komplettes BSI-IT-Grundschutz-Plugin mit Baustein-Modellierung
- Schutzbedarfs-Mapping (pro Control konfigurierbar)
- Report-Export passend zu BSI-Berichtsformaten

---

## 5. Regulierter Mittelstand (200 - 5000 Mitarbeiter)

**Primaere Regulierungen:**

- **ISO/IEC 27001** (internationale Zertifizierung)
- **TISAX** (Automotive-Supply-Chain)
- DSGVO
- Kunden-spezifische SLA-Anforderungen
- Branchenspezifisch: NIS2 (wenn kritische Einrichtung)

**Typische Anforderungen:**

- Zertifizierungs-Vorbereitung (Stage 1 / Stage 2 Audits)
- Kontinuierliches ISMS ohne eigenes grosses Compliance-Team
- Toolgestuetzte Findings-Pflege, um mit 1-2 FTE Compliance zu skalieren

**Wie ComplianceOS unterstuetzt:**

- ISO 27001:2022 Annex A (93 Controls) vollstaendig abgebildet
- TISAX-Fragenkataloge laden und abarbeiten (Import-Pipeline)
- Remediation-Tracking mit Deadlines + Verantwortlichen
- Dashboard fuer ISB/CISO mit Trend-Visualisierung

---

## Was alle gemeinsam haben

Alle fuenf Zielgruppen haben vier Anforderungen gemein:

1. **Audit-Daten muessen on-premise bleiben** — rechtlich oder politisch
   keine Public-Cloud-Option fuer den Audit-Korpus selbst.
2. **Mehrere Standards parallel erfuellen** — kaum eine Organisation muss
   nur ein Regelwerk adressieren. Cross-Standard-Mapping spart Arbeit.
3. **Nachvollziehbarkeit > LLM-Magie** — Pruefer und Auditoren fordern
   dokumentierte Standard-Referenzen pro Aussage, keine KI-Halluzinationen.
4. **Geringe Infrastructure-Last** — Compliance-Tools duerfen kein
   eigenstaendiges Team fuer Betrieb/Hosting erfordern.

ComplianceOS ist fuer genau diese Einschraenkungen designed:
19 MB Alpine-Container, SQLite (keine separate DB), null Telemetrie, volle
Standard-Referenz-Kette pro Finding.
