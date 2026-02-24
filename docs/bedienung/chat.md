# Chat

Der KI-Chat ist Ihr persoenlicher Compliance-Berater. Stellen Sie Fragen zu Standards, lassen Sie Findings analysieren oder holen Sie sich Empfehlungen.

![Chat Uebersicht](../screenshots/chat/chat-overview.png)

!!! info "Voraussetzung"
    Der Chat erfordert eine Claude Code Installation und `ENABLE_TEAMMATES=true`.
    Ohne KI-Integration stehen vorgefertigte Antworten zu haeufigen Fragen bereit.

## Chat starten

1. Klicken Sie auf **Chat** in der Seitenleiste
2. Geben Sie Ihre Frage ein
3. Die Antwort wird in Echtzeit gestreamt

## Was koennen Sie fragen?

ComplianceOS erkennt 9 verschiedene Frage-Typen automatisch:

| Intent | Beispiel |
|--------|---------|
| **Audit** | "Starte einen Audit fuer die Domain CRYPTO" |
| **Findings** | "Zeige mir alle offenen Major NCs" |
| **Standard** | "Was fordert ISO 27001 Annex A.8.24?" |
| **Policy** | "Generiere eine Passwort-Richtlinie" |
| **Risk** | "Wie hoch ist das Risiko bei fehlender Verschluesselung?" |
| **Report** | "Erstelle einen Executive Summary" |
| **Compare** | "Vergleiche die letzten zwei Audit-Laeufe" |
| **Help** | "Wie funktioniert die Drift-Detection?" |
| **General** | Alle anderen Compliance-Fragen |

## Sessions

Jede Konversation wird als Session gespeichert. Sie koennen:

- Fruehere Sessions wieder oeffnen
- Den Verlauf einsehen
- Sessions loeschen

## Beispiel-Dialoge

**Frage:** "Welche Controls sind in der Domain ACCESS nicht erfuellt?"

Der Assistent analysiert Ihre aktuellen Findings und listet die betroffenen Controls mit Empfehlungen auf.

**Frage:** "Erklaere mir den Unterschied zwischen ISO 27001 und NIS2"

Der Assistent erklaert die Unterschiede mit Bezug auf die in ComplianceOS abgebildeten Controls.
