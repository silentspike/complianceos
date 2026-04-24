# Architektur

ComplianceOS ist eine On-Premise Compliance-Audit-Plattform. Die Anwendung
laeuft vollstaendig auf der Infrastruktur des Kunden — Audit-Daten, Dokumente
und Reports verlassen das Kunden-Netzwerk nicht.

## Pipeline

Der Audit-Durchlauf folgt einem standardisierten Fluss:

```
 ┌──────────┐     ┌─────────┐     ┌─────────┐     ┌──────────┐     ┌──────────┐     ┌────────┐
 │  Ingest  │ ──▶ │  Parse  │ ──▶ │ Extract │ ──▶ │  Match   │ ──▶ │ Findings │ ──▶ │ Report │
 │          │     │         │     │         │     │ (Matrix) │     │          │     │        │
 └──────────┘     └─────────┘     └─────────┘     └──────────┘     └──────────┘     └────────┘
   Upload:          PDF/DOCX        Semantische      135 Controls     Severity +       Markdown
   PDF, DOCX,       Konvertierung   Claims aus       in 12 Domains    Confidence       + HTML
   XLSX, MD, TXT    -> Text         Dokument                          + Evidence       + PDF
```

**Stage-Beschreibung:**

| Stage | Funktion |
|---|---|
| **Ingest** | Dokument-Upload (PDF, DOCX, XLSX, Markdown, Plaintext). Eingangspruefung: Dateityp, Groesse, nicht-ausfuehrbar. |
| **Parse** | Dokument-zu-Text-Konvertierung (PyMuPDF, python-docx, openpyxl). Tabellen werden als Markdown-Tabellen erhalten, Kapitel-Struktur als Headings extrahiert. |
| **Extract** | Semantische Extraktion von Compliance-Claims. Deterministische Regex-Regeln plus optionaler LLM-Assist (Claude BYOK) fuer komplexe Formulierungen. |
| **Match** | Abgleich der Claims mit der Control-Matrix (135 Controls x 2246 AUDIT-CHECKs). Jeder Match erhaelt einen Confidence-Score (0-100). |
| **Findings** | Pruefergebnisse werden als Findings persistiert: Severity (major/minor/observation/ofi), Confidence, Evidence-Zitat, Reasoning, betroffenes Control. |
| **Report** | Formale Ausgabe als Markdown (primaer) bzw. PDF/HTML (Export). Report folgt ISO 27001 Audit-Report-Konvention: Scope, Methodik, Findings je Domain, Management-Summary. |

## 12 Domains

Jedes Control ist genau einer der folgenden 12 technischen Domains zugeordnet:

| Domain | Fokus |
|---|---|
| **CRYPTO** | Kryptographie, TLS, Key-Management, Signaturen |
| **ACCESS** | Authentifizierung, Autorisierung, RBAC, MFA |
| **BACKUP** | Datensicherung, Retention, 3-2-1-Strategie, Restore-Tests |
| **LOGGING** | Audit-Logs, Log-Retention, SIEM-Integration, Tamper-Resistance |
| **NETWORK** | Netz-Segmentierung, Firewall, Ingress/Egress, VPN |
| **INCIDENT** | Incident Response, IRP, Forensics, Breach-Notification |
| **VULN** | Vulnerability Management, Patch-Prozesse, Pen-Tests |
| **BCP** | Business Continuity, DR, RPO/RTO, BIA |
| **SUPPLY** | Supply-Chain, Third-Party-Risk, SBOM |
| **PII** | Personal Identifiable Information, Data Privacy, DSGVO |
| **CONFIG** | Konfigurationsmanagement, Hardening, Baselines |
| **MALWARE** | Anti-Malware, EDR, Execution-Control |

## 9 Standards

ComplianceOS mapped seine 135 Controls cross-standard auf die folgenden
Regelwerke. Ein Control kann mehrere Standards gleichzeitig adressieren —
das reduziert Doppelarbeit bei Organisationen mit mehreren Zertifizierungen.

| Standard | Version | Scope |
|---|---|---|
| **ISO/IEC 27001** | 2022 | Information Security Management System (ISMS), Annex A mit 93 Controls |
| **ISO 22301** | 2019 | Business Continuity Management System (BCMS), BIA, RPO/RTO |
| **ISO/IEC 27005** | 2022 | Informationssicherheits-Risikomanagement |
| **ISO/IEC 27017** | 2015 | Cloud-Security-Controls fuer Cloud-Services |
| **ISO/IEC 27018** | 2019 | Schutz personenbezogener Daten in Public Clouds |
| **ISO/IEC 27035** | 2023 | Incident-Management-Prozess |
| **NIS2** | EU 2022/2555 | EU-Richtlinie fuer kritische und wichtige Einrichtungen |
| **BSI IT-Grundschutz** | 2023 Kompendium | Baustein-basiertes Schutzprofil (Deutschland) |
| **DSGVO** | EU 2016/679 | Europaeische Datenschutzgrundverordnung |

## Governance-Logik

Jedes Control ist kein freies LLM-Output, sondern an einen Standard-Paragraph
gebunden. Bei der Ausgabe eines Findings liefert ComplianceOS immer eine
nachvollziehbare Kette:

```
Finding  ─▶  Control (z. B. CRYPTO-001)  ─▶  Standard-Referenz (z. B. ISO 27001 Annex A.8.24)
                                        ─▶  Semantische AUDIT-CHECKs (Pruefpunkte)
                                        ─▶  Evidence (Zitat aus Upload-Dokument)
                                        ─▶  Confidence-Score (0-100)
```

LLM-Assist (optional, Claude BYOK) wird nur in der Extract-Stage und im Chat-
Assistenten verwendet — nie um Standard-Referenzen zu generieren. Die 2246
AUDIT-CHECKs sind kuratierte Prueflisten, keine KI-Halluzinationen.

## Datenhaltung

- **Datenbank:** SQLite (WAL-Modus) — eine Datei auf der Kunden-Infrastruktur
- **Dokumente:** Lokaler Datastore innerhalb des Docker-Volumes bzw. deployten
  Pfads
- **Kein Daten-Export nach aussen** — weder Telemetrie noch anonymisierte
  Nutzungsdaten verlassen die Installation
- **Optional LLM-Anbindung:** nur wenn Kunde einen Anthropic-API-Key
  hinterlegt ("Bring Your Own Key"-Muster). Dann werden einzelne
  Audit-Pruefpunkte und Chat-Anfragen uebertragen — **nicht** Dokument-
  Volltexte, Reports oder Datenbank-Inhalte

## Architektur-Schichten

```
┌────────────────────────────────────────────────────────────────┐
│  Interface-Schicht (HTTP, htmx, Server-Sent Events)            │
│  - /api/audits, /api/findings, /api/documents, /api/chat       │
│  - Web-UI (Dashboard, Findings-Browser, Chat)                  │
└────────────────────────────────────────────────────────────────┘
                              │
┌────────────────────────────────────────────────────────────────┐
│  Application-Schicht (Use-Cases)                               │
│  - Audit-Runner, Document-Parser, Chat-Handler                 │
│  - Policy-Generator, Drift-Detector, Report-Exporter           │
└────────────────────────────────────────────────────────────────┘
                              │
┌────────────────────────────────────────────────────────────────┐
│  Domain-Schicht (Compliance-Modell)                            │
│  - Control, Finding, Evidence, Matrix, Standard                │
│  - Cross-Standard-Mapping                                       │
└────────────────────────────────────────────────────────────────┘
                              │
┌────────────────────────────────────────────────────────────────┐
│  Infrastructure-Schicht                                        │
│  - SQLite, LLM-Gateway, PDF-Renderer, Notifier (SMTP/ntfy)     │
│  - License-Server (WP-18)                                      │
└────────────────────────────────────────────────────────────────┘
```

## Deployment-Modell

| Aspekt | Wert |
|---|---|
| Deployment | On-Premise Container (19 MB Alpine-Image) oder Single-Binary |
| Ressourcen | 512 MB RAM, 1 GB Disk (typisch); skaliert mit Auditvolumen |
| Netzwerk | Eine TCP-Port-Oeffnung fuer Web-UI (default 8001) |
| Datenbank | Keine separate DB-Instanz noetig (SQLite) |
| Abhaengigkeiten | Optional: Anthropic-API-Key fuer LLM-Features; sonst null externe Dependencies zur Laufzeit |

## Roadmap-Hinweise

- **v1.0.x:** Go-Port als Production-Stand; Python-Legacy-Stand verbleibt als
  Referenz im `python-legacy/`-Verzeichnis des Source-Repos
- **v1.1:** Lokale LLM-Unterstuetzung (Ollama) als Alternative zu Anthropic
  BYOK — fuer Kunden die keinerlei Cloud-API nutzen wollen
- **v1.2:** Erweiterte BCP-Module (ISO 22301 Szenario-Uebungen)

## Privacy-Hinweis

Alle Homelab-, Kunden- und Deployment-spezifischen Konfigurationen bleiben
on-premise. Die im oeffentlichen Repo beigefuegte Control-Matrix
(`assets/control-matrix.yaml`) ist eine **Template-Version mit Platzhaltern**
(`<PROXMOX_NODE_IP>`, `<INTERNAL_NETWORK>`, `<TENANT_ID>`). Kunden-spezifische
Matrizen koennen zur Laufzeit via Umgebungsvariable
`COMPLIANCEOS_CONTROL_MATRIX=/pfad/zu/kunden-matrix.yaml` eingebunden werden
ohne Rebuild.
