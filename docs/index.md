# Willkommen bei ComplianceOS

**ComplianceOS** ist eine On-Premise-Plattform fuer automatisierte Compliance-Audits gegen 9 internationale Sicherheitsstandards. Die Anwendung laeuft vollstaendig auf Ihrer eigenen Infrastruktur.

![ComplianceOS Dashboard](screenshots/dashboard/dashboard-overview.png)

## Was kann ComplianceOS?

- **Audits durchfuehren** gegen ISO 27001, NIS2, BSI IT-Grundschutz und 6 weitere Standards
- **Findings verwalten** mit Severity-Klassifikation und Status-Workflow
- **Massnahmen verfolgen** mit Zuweisung, Deadlines und Fortschrittsmessung
- **Policies generieren** aus 6 vorgefertigten Vorlagen
- **KI-Beratung** erhalten ueber den integrierten Chat (optional, Claude AI)
- **Drift erkennen** zwischen aufeinanderfolgenden Audit-Laeufen
- **Reports erstellen** fuer Management und externe Auditoren

## Schnellstart

```bash
git clone https://github.com/silentspike/complianceos.git
cd complianceos
docker compose up -d
```

Dann oeffnen Sie [http://localhost:8001](http://localhost:8001) im Browser.

!!! tip "Erster Schritt"
    Nach dem Start legen Sie ein Projekt an und fuehren Ihren ersten Audit durch.
    Folgen Sie dazu der Anleitung unter [Erste Schritte](schnellstart/erste-schritte.md).

## Uebersicht

| Bereich | Beschreibung |
|---------|-------------|
| [Dashboard](bedienung/dashboard.md) | Compliance-Score, Domain-Uebersicht, aktuelle Findings |
| [Audits](bedienung/audits.md) | Audit starten, Fortschritt verfolgen, Ergebnisse einsehen |
| [Findings](bedienung/findings.md) | Findings filtern, Details ansehen, Status aendern |
| [Remediation](bedienung/remediation.md) | Massnahmen zuweisen und verfolgen |
| [Chat](bedienung/chat.md) | KI-gestuetzte Compliance-Beratung |
| [Dokumente](bedienung/dokumente.md) | Dokumente hochladen und analysieren |
| [Policies](bedienung/policies.md) | Richtlinien generieren und verwalten |
| [Reports](bedienung/reports.md) | Berichte erstellen und exportieren |
| [Executive](bedienung/executive.md) | Management-Dashboard mit Risiko-Matrix |
| [Einstellungen](bedienung/einstellungen.md) | Praeferenzen, Projekte, System-Info |
