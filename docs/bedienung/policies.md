# Policies

ComplianceOS kann Richtlinien-Dokumente aus Vorlagen generieren. Diese koennen als Ausgangspunkt fuer Ihre organisationsspezifischen Policies dienen.

![Policies Uebersicht](../screenshots/policies/policies-overview.png)

## Verfuegbare Vorlagen

| Vorlage | Beschreibung |
|---------|-------------|
| **Passwort-Richtlinie** | Passwort-Anforderungen, MFA, Sperrung |
| **Backup-Richtlinie** | Sicherungsintervalle, Aufbewahrung, Tests |
| **Incident-Richtlinie** | Meldewege, Eskalation, Dokumentation |
| **Zugriffs-Richtlinie** | Least Privilege, Rollen, Reviews |
| **ISMS-Richtlinie** | Informationssicherheits-Managementsystem |
| **Datenschutz-Richtlinie** | DSGVO-Anforderungen, Verarbeitungstaetigkeiten |

## Policy generieren

1. Navigieren Sie zu **Policies** in der Seitenleiste
2. Waehlen Sie eine Vorlage aus dem Dropdown
3. Klicken Sie auf **Generieren**

Die generierte Policy erscheint sofort in der Detailansicht.

## Detailansicht

Generierte Policies werden als Markdown angezeigt und enthalten:

- Geltungsbereich
- Verantwortlichkeiten
- Konkrete Anforderungen
- Standard-Referenzen (ISO, NIS2, BSI)
- Inkrafttreten und Review-Zyklus

## Policies verwalten

Alle generierten Policies werden gespeichert und koennen:

- Jederzeit wieder eingesehen werden
- Als Grundlage fuer Ihre eigenen Dokumente dienen
- Mit Control-Mappings verknuepft werden

!!! tip "Anpassung"
    Die generierten Policies sind Vorlagen. Passen Sie diese an Ihre
    Organisation an, bevor Sie sie offiziell in Kraft setzen.
