# Erste Schritte

Nach der Installation fuehrt diese Anleitung Sie durch die wichtigsten Funktionen.

## 1. Projekt anlegen

Nach dem ersten Start sehen Sie ein leeres Dashboard. ComplianceOS arbeitet projektbezogen — jedes Projekt repraesentiert eine Organisation oder einen Audit-Scope.

1. Oeffnen Sie **Einstellungen** in der Seitenleiste
2. Klicken Sie auf **Neues Projekt**
3. Geben Sie einen Namen und optional eine Beschreibung ein
4. Klicken Sie auf **Erstellen**

Das Projekt ist jetzt aktiv und Sie koennen Audits durchfuehren.

## 2. Ersten Audit starten

1. Klicken Sie auf **Audits** in der Seitenleiste
2. Waehlen Sie den Modus:
   - **Vollaudit**: Alle 135 Controls werden geprueft
   - **Domain-Audit**: Nur eine bestimmte Domain (z.B. CRYPTO, ACCESS, BACKUP)
3. Klicken Sie auf **Audit starten**

!!! info "Dauer"
    Ein Vollaudit dauert je nach System 1-5 Minuten.
    Ein Domain-Audit ist in wenigen Sekunden abgeschlossen.

## 3. Ergebnisse ansehen

Nach Abschluss des Audits:

1. Auf dem **Dashboard** sehen Sie den Compliance-Score als Ring-Diagramm
2. Unter **Findings** finden Sie alle identifizierten Abweichungen
3. Jedes Finding hat eine Severity:
   - **Major NC** — Schwerwiegende Nichtkonformitaet
   - **Minor NC** — Geringfuegige Nichtkonformitaet
   - **Observation** — Beobachtung / Verbesserungspotenzial
   - **OFI** — Opportunity for Improvement

## 4. Findings bearbeiten

1. Klicken Sie auf ein Finding fuer die Detailansicht
2. Sie sehen: Beschreibung, Empfehlung, Evidence, Reasoning
3. Aendern Sie den Status: Open → In Progress → Resolved → Accepted

## 5. Naechste Schritte

- [Dashboard](../bedienung/dashboard.md) verstehen
- [Policy generieren](../bedienung/policies.md) fuer identifizierte Luecken
- [KI-Chat](../bedienung/chat.md) fuer Compliance-Fragen nutzen
- [Remediation](../bedienung/remediation.md) fuer Massnahmen-Tracking einrichten
