# AI Deployment in Regulated Environments

Compliance-Audits sind sensibles Terrain fuer KI-Integration. Daten duerfen
nicht in die Cloud, Audit-Trails muessen nachvollziehbar bleiben, regulatorische
Anforderungen (DSGVO Art. 25, BSI C5, NIS2 Art. 21) verlangen klare technische
und organisatorische Massnahmen. ComplianceOS ist gegen genau dieses
Spannungsfeld designed.

## On-Prem AI Boundary

Compliance-Daten verlassen die Kunden-Infrastruktur nicht.

- Optional Claude API integration: nur Audit-Pruefpunkte und Findings-Analysen
  werden gesendet
- Dokumente, Reports und Datenbank bleiben lokal
- Konkretisierung: SQLite lokal, Document-Pipeline laeuft auf der
  Kunden-Infrastruktur, kein outbound traffic im default Setup

## Optional AI Integration (Privacy-First)

KI-Integration ist abschaltbar.

- `ENABLE_TEAMMATES=false` deaktiviert die KI-Integration komplett
- Kein Telemetrie, kein Tracking
- Disclosure transparent dokumentiert in der README-Datenschutz-Section

## No-Telemetry

Keine externe Datenuebertragung.

- SQLite lokal — keine externe Datenbank
- Audit-Trail bleibt im Customer-Hosting
- Logging ueber lokale Pipelines (Loki/Grafana wenn vorhanden, sonst Filesystem)

## Regulated Evaluation Flow

Pilot-Modell ist auf regulierte Branchen zugeschnitten.

- 90-Tage-Pilot auf der Kunden-Infrastruktur
- Vollstaendige Audit-Artefakte fuer den ersten Compliance-Zyklus (Asset-Inventar,
  Risk-Register, Policy-Set, Remediation-Plan)
- Klar dokumentierte Reifegrade: ISMS-Aufbau, Asset-Management, Risk-Treatment

## Pilot Model

EULA-basiert, persoenliche Begleitung.

- EULA-basiertes Lizenzmodell (siehe [Evaluation anfordern](https://github.com/silentspike/complianceos/issues/new?template=evaluation_request.yml))
- Begleitung durch silentspike (fachlich + regulatorisch)
- Skalierbar nach Pilot — Lizenz-Renewal pro Audit-Zyklus oder per-Standard

## Bottom Line

Wenn Sie KI in einer regulierten Umgebung einsetzen wollen, ist die
Architektur-Frage *zuerst* eine Boundary-Frage und *danach* eine Modell-Frage.
ComplianceOS definiert die Boundary explizit und macht die optionale
KI-Integration zu einem abschaltbaren Add-on, nicht zu einer Voraussetzung.

## Verweise

- [Architektur-Ueberblick](../architecture.md)
- [Control-Matrix Workflow](../architecture/control-matrix-workflow.md)
- [Datenschutz-Hinweise im README](https://github.com/silentspike/complianceos#datenschutz)
- [Evaluation Request Template](https://github.com/silentspike/complianceos/issues/new?template=evaluation_request.yml)
