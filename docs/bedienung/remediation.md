# Remediation

Das Remediation-Modul hilft Ihnen, Massnahmen zur Behebung von Findings zu planen, zuzuweisen und nachzuverfolgen. Drei Ansichten bieten unterschiedliche Perspektiven auf den Fortschritt.

---

## Kanban-Board

Die Standard-Ansicht zeigt ein **Kanban-Board** mit vier Spalten:

<figure class="screenshot" markdown>
![Remediation Kanban](../screenshots/findings/remediation-overview.png)
<figcaption>Kanban-Board: Findings nach Status sortiert mit Severity-Badges, Priorität und Burndown-Chart</figcaption>
</figure>

| Spalte | Bedeutung | Farbe |
|--------|-----------|-------|
| **Offen** | Finding identifiziert, noch keine Massnahme begonnen | Rot |
| **In Arbeit** | Massnahme wird aktiv umgesetzt | Orange |
| **Behoben** | Massnahme umgesetzt, wartet auf Verifikation | Blau |
| **Akzeptiert** | Verifiziert und abgeschlossen | Grün |

Jede Karte zeigt:

- **Severity-Badge** (Major NC, Minor NC, Observation, OFI)
- **Control-ID** und Kurztitel
- **Priorität** (Critical, High, Medium, Low)
- **Zuständiger** (wenn zugewiesen)
- **Deadline** (wenn gesetzt)

### Burndown-Chart

Unterhalb des Kanban-Boards zeigt der **Burndown-Chart** den Fortschritt über die Zeit:

- **X-Achse**: Zeitverlauf (Tage/Wochen)
- **Y-Achse**: Anzahl offener Findings
- **Trend-Linie**: Zeigt ob Sie auf Kurs sind

---

## Listen-Ansicht

Die Listen-Ansicht zeigt alle Findings als sortierbare Tabelle:

<figure class="screenshot" markdown>
![Remediation Liste](../screenshots/findings/remediation-list.png)
<figcaption>Listen-Ansicht: Tabellarische Darstellung mit Severity, Domain, Status, Priorität und Deadline</figcaption>
</figure>

| Spalte | Beschreibung | Sortierbar |
|--------|-------------|------------|
| **Severity** | Schweregrad des Findings | Ja |
| **Control** | Control-ID und Kurzname | Ja |
| **Domain** | Sicherheitsbereich | Ja |
| **Status** | Aktueller Bearbeitungsstand | Ja |
| **Priorität** | Zugewiesene Priorität | Ja |
| **Zuständiger** | Verantwortliche Person | Ja |
| **Deadline** | Fälligkeitsdatum | Ja |

Die Listen-Ansicht eignet sich besonders für:

- Sortierung nach Priorität oder Deadline
- Schnellen Überblick über alle offenen Massnahmen
- Export-Vorbereitung (CSV)

---

## Kalender-Ansicht

Die Kalender-Ansicht zeigt Findings nach ihrem Fälligkeitsdatum:

<figure class="screenshot" markdown>
![Remediation Kalender](../screenshots/findings/remediation-calendar.png)
<figcaption>Kalender-Ansicht: Findings mit Deadlines im Monatskalender und Burndown-Chart</figcaption>
</figure>

- **Monats-Kalender** mit farbcodierten Findings an ihren Deadlines
- **Severity-Farben** zur schnellen Erkennung von Major NCs
- **Burndown-Chart** auch in der Kalender-Ansicht verfügbar

!!! tip "Deadline-Management"
    Die Kalender-Ansicht hilft bei der Planung: Sehen Sie auf einen Blick welche Deadlines in den nächsten Wochen anstehen und ob Engpässe drohen.

---

## Massnahme erstellen und zuweisen

### Aus der Finding-Detailansicht

1. Öffnen Sie ein Finding in der Detailansicht
2. Im Bereich **Remediation-Status** sehen Sie die aktuellen Zuweisungen
3. Setzen Sie:
      - **Verantwortlich**: Name der zuständigen Person
      - **Priorität**: Critical, High, Medium oder Low
      - **Deadline**: Fälligkeitsdatum
      - **Geschätzter Aufwand**: In Stunden
4. Klicken Sie auf **Speichern**

### Prioritäten und Fristen

| Priorität | Farbe | Ziel-Behebungszeit | Empfohlener Einsatz |
|-----------|-------|-------------------|-------------------|
| **Critical** | Rot | 7 Tage | Major NCs mit direktem Risiko |
| **High** | Orange | 30 Tage | Major NCs, sicherheitskritische Minor NCs |
| **Medium** | Gelb | 90 Tage | Minor NCs, wichtige Observations |
| **Low** | Grau | Nach Bedarf | OFIs, optionale Verbesserungen |

!!! warning "Major NCs"
    Major NCs sollten immer mindestens als **High** priorisiert werden. Bei direkter Gefahrenlage ist **Critical** angemessen.

---

## Verifikation

Nach Abschluss einer Massnahme folgt die Verifikation:

1. **Massnahme umsetzen**: Technische oder organisatorische Änderung durchführen
2. **Status auf "Behoben" setzen**: Signalisiert dass die Massnahme abgeschlossen ist
3. **Domain-Audit durchführen**: Gezielter Nachtest der betroffenen Domain
4. **Ergebnis prüfen**:
      - Finding nicht mehr vorhanden → Status auf **"Akzeptiert"** setzen
      - Finding weiterhin vorhanden → Status zurück auf **"In Arbeit"** mit Kommentar

```mermaid
flowchart LR
    A[Massnahme<br/>umsetzen] --> B[Status:<br/>Behoben]
    B --> C[Domain-Audit<br/>durchfuehren]
    C -->|Finding weg| D[Status:<br/>Akzeptiert]
    C -->|Finding noch da| E[Status:<br/>In Arbeit]
    E --> A
    style D fill:#1a1a2e,stroke:#10b981,color:#e2e8f0
    style E fill:#1a1a2e,stroke:#f59e0b,color:#e2e8f0
```

---

## Team-Mitglieder

Unter **Einstellungen > Team** können Sie Mitarbeiter anlegen die als Verantwortliche für Findings zugewiesen werden können:

- **Name**: Anzeigename im System
- **Rolle**: Position oder Funktion
- **E-Mail**: Für Benachrichtigungen (optional)

Die angelegten Teammitglieder stehen dann im Dropdown "Verantwortlich" bei jedem Finding zur Verfügung.

---

## Aktivitäts-Log

Jede Statusänderung wird im Aktivitäts-Log des Findings protokolliert:

- **Zeitstempel**: Wann die Änderung erfolgte
- **Akteur**: Wer die Änderung vorgenommen hat
- **Aktion**: Was geändert wurde (Status, Priorität, Zuweisung)
- **Kommentar**: Optionale Begründung

Das Log bietet eine lückenlose Nachverfolgbarkeit — wichtig für externe Audits und Compliance-Nachweise.

---

## Tipps für effektives Remediation-Tracking

!!! tip "Priorisierung"
    Beginnen Sie mit Major NCs und arbeiten Sie sich nach unten vor. Nutzen Sie die Listen-Ansicht mit Sortierung nach Severity für eine klare Reihenfolge.

!!! tip "Regelmässige Reviews"
    Führen Sie wöchentliche Reviews des Kanban-Boards durch. Prüfen Sie: Stagnieren Findings in "In Arbeit"? Sind Deadlines gefährdet? Gibt es Blocker?

!!! tip "Verifikation nicht vergessen"
    Ein Finding auf "Behoben" zu setzen reicht nicht. Führen Sie immer einen [Domain-Audit](audits.md) zur Verifikation durch bevor Sie den Status auf "Akzeptiert" ändern.

!!! tip "Benachrichtigungen"
    Richten Sie [ntfy-Benachrichtigungen](einstellungen.md) ein um bei Statusänderungen oder nahenden Deadlines automatisch informiert zu werden.
