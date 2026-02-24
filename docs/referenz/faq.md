# FAQ

## Allgemein

### Was ist ComplianceOS?
ComplianceOS ist eine On-Premise-Plattform fuer automatisierte Compliance-Audits. Sie prueft Ihre IT-Infrastruktur gegen 9 internationale Standards und hilft bei der Behebung von Abweichungen.

### Ersetzt ComplianceOS einen externen Auditor?
Nein. ComplianceOS ist ein Werkzeug zur Vorbereitung und Durchfuehrung interner Audits. Fuer offizielle Zertifizierungen (z.B. ISO 27001) benoetigen Sie weiterhin einen akkreditierten Auditor.

### Welche Daten verlassen mein System?
Ohne KI-Integration: Keine. Mit KI-Integration: Audit-Pruefpunkte und Chat-Nachrichten werden an die Claude API gesendet. Siehe [Datenschutz](../schnellstart/datenschutz.md).

## Installation

### Welche Systemvoraussetzungen gibt es?
Docker und Docker Compose, mindestens 512 MB RAM und 1 GB Festplatte. Siehe [Installation](../schnellstart/installation.md).

### Kann ich ComplianceOS ohne Docker betreiben?
ComplianceOS wird als Docker-Image ausgeliefert. Der Betrieb ohne Docker wird nicht unterstuetzt.

### Wie aktualisiere ich auf eine neue Version?
```bash
docker compose pull
docker compose up -d
```

## Audits

### Wie lange dauert ein Vollaudit?
Je nach System 1-5 Minuten fuer alle 135 Controls.

### Kann ich nur einen Teilbereich pruefen?
Ja, waehlen Sie beim Audit-Start den Modus "Domain-Audit" und eine spezifische Domain.

### Was bedeutet der Confidence-Wert?
Der Confidence-Wert (0-100%) zeigt, wie zuverlaessig die automatische Bewertung ist. Niedrige Werte deuten darauf hin, dass eine manuelle Pruefung empfohlen wird.

## Findings

### Was ist der Unterschied zwischen Major NC und Minor NC?
- **Major NC:** Schwerwiegende Abweichung, die die Wirksamkeit des Managementsystems gefaehrdet
- **Minor NC:** Geringfuegige Abweichung, die das System nicht grundsaetzlich in Frage stellt

### Kann ich Findings exportieren?
Ja, der Findings-Browser hat eine CSV-Export-Funktion.

## KI-Integration

### Ist die KI-Integration Pflicht?
Nein. Alle Kernfunktionen (Audits, Findings, Policies, Reports) arbeiten vollstaendig ohne KI. Der Chat-Assistent nutzt vorgefertigte Antworten, wenn keine KI verfuegbar ist.

### Welche KI wird verwendet?
Claude von Anthropic. Sie benoetigen eine Claude Code Subscription.

### Kann ich eine andere KI verwenden?
Derzeit wird nur Claude unterstuetzt. Weitere Anbieter koennen in zukuenftigen Versionen folgen.
