# Remediation

Das Remediation-Modul hilft Ihnen, Massnahmen zur Behebung von Findings zu planen, zuzuweisen und zu verfolgen.

![Remediation Uebersicht](../screenshots/findings/remediation-overview.png)

## Massnahme erstellen

1. Oeffnen Sie ein Finding
2. Klicken Sie auf **Massnahme erstellen**
3. Fuellen Sie aus:
   - **Verantwortlich:** Name der zustaendigen Person
   - **Prioritaet:** Critical, High, Medium, Low
   - **Deadline:** Faelligkeitsdatum
   - **Geschaetzter Aufwand:** In Stunden
4. Klicken Sie auf **Erstellen**

## Uebersicht

Die Remediation-Uebersicht zeigt alle offenen Massnahmen mit:

- Zustaendigem Mitarbeiter
- Prioritaet und Deadline
- Aktueller Status
- Zugehoeriges Finding

## Prioritaeten

| Prioritaet | Ziel-Behebungszeit | Farbe |
|-----------|-------------------|-------|
| **Critical** | 7 Tage | Rot |
| **High** | 30 Tage | Orange |
| **Medium** | 90 Tage | Gelb |
| **Low** | Nach Bedarf | Grau |

## Verifikation

Nach Abschluss einer Massnahme:

1. Setzen Sie den Status auf **Resolved**
2. Ein Verifizierer prueft die Umsetzung
3. Bei erfolgreicher Pruefung: Status auf **Accepted**
4. Bei Maengeln: Zurueck auf **In Progress** mit Kommentar

## Team-Mitglieder

Unter **Einstellungen > Team** koennen Sie Mitarbeiter anlegen, die als Verantwortliche zugewiesen werden koennen.

!!! tip "Aktivitaets-Log"
    Jede Statusaenderung wird im Aktivitaets-Log des Findings protokolliert —
    mit Zeitstempel, Akteur und optionalem Kommentar.
