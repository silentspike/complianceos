# FAQ

Haeufig gestellte Fragen zu ComplianceOS — sortiert nach Themenbereichen.

---

## Allgemein

### Was ist ComplianceOS?

ComplianceOS ist eine On-Premise-Plattform fuer automatisierte Compliance-Audits. Sie prueft Ihre IT-Infrastruktur gegen 9 internationale Standards (ISO 27001, NIS2, BSI IT-Grundschutz und weitere) und hilft bei der Identifikation und Behebung von Abweichungen.

### Fuer wen ist ComplianceOS gedacht?

ComplianceOS richtet sich an:

- **Compliance-Beauftragte** die regelmaessig interne Audits durchfuehren
- **CISOs und IT-Sicherheitsverantwortliche** die den Compliance-Zustand ueberwachen
- **Geschaeftsfuehrung** die einen Ueberblick ueber Risiken und Compliance-Stand benoetigt
- **IT-Teams** die Sicherheitsmassnahmen umsetzen und nachverfolgen

### Ersetzt ComplianceOS einen externen Auditor?

Nein. ComplianceOS ist ein Werkzeug zur Vorbereitung und Durchfuehrung **interner Audits**. Fuer offizielle Zertifizierungen (z.B. ISO 27001) benoetigen Sie weiterhin einen akkreditierten externen Auditor. ComplianceOS hilft Ihnen jedoch, optimal auf ein externes Audit vorbereitet zu sein.

### Welche Daten verlassen mein System?

- **Ohne KI-Integration**: Keine Daten verlassen Ihr System
- **Mit KI-Integration**: Audit-Pruefpunkte und Chat-Nachrichten werden an die Claude API (Anthropic) gesendet
- **Nie gesendet**: Hochgeladene Dokumente, Passwort-Richtlinien, personenbezogene Daten, OAuth-Tokens

Details: [Datenschutz](../schnellstart/datenschutz.md)

### Ist ComplianceOS kostenlos?

ComplianceOS ist unter der Apache-2.0-Lizenz frei verfuegbar. Die optionale KI-Integration erfordert eine Claude Code Subscription von Anthropic.

---

## Installation und Betrieb

### Welche Systemvoraussetzungen gibt es?

| Komponente | Minimum | Empfohlen |
|-----------|---------|-----------|
| Docker + Docker Compose | Pflicht | Aktuelle Version |
| RAM | 256 MB | 512 MB - 1 GB |
| Festplatte | 100 MB | 1-5 GB |
| Browser | Chromium-basiert | Chrome, Edge, Firefox |

Details: [Installation](../schnellstart/installation.md)

### Kann ich ComplianceOS ohne Docker betreiben?

Ja, ComplianceOS kann auch direkt mit Python betrieben werden:

```bash
pip install -e ".[docs]"
make dev
```

Docker ist die empfohlene Methode fuer den produktiven Einsatz. Details: [Installation](../schnellstart/installation.md)

### Wie aktualisiere ich auf eine neue Version?

```bash
cd complianceos
git pull
docker compose build
docker compose up -d
```

Datenbank-Migrationen werden automatisch beim Start durchgefuehrt. Bestehende Daten bleiben erhalten.

### Wie erstelle ich ein Backup?

```bash
docker run --rm \
  -v complianceos_complianceos-data:/data \
  -v $(pwd):/backup \
  busybox tar czf /backup/complianceos-backup-$(date +%Y%m%d).tar.gz /data
```

Details: [Docker-Konfiguration](../schnellstart/docker.md)

### Kann ich den Port aendern?

Ja, in der `docker-compose.yml`:

```yaml
ports:
  - "9000:8001"  # Externer Port 9000
```

---

## Audits

### Wie lange dauert ein Vollaudit?

Abhaengig von der Systemleistung und KI-Verfuegbarkeit:

- **Vollaudit**: 1-5 Minuten fuer alle 135 Controls
- **Domain-Audit**: 10-60 Sekunden

### Kann ich nur einen Teilbereich pruefen?

Ja, waehlen Sie beim Audit-Start den Modus **Domain-Audit** und eine der 12 Domains (z.B. CRYPTO, ACCESS, BACKUP). So pruefen Sie gezielt einen einzelnen Sicherheitsbereich.

### Wie oft sollte ich Audits durchfuehren?

- **Empfohlen**: Mindestens monatlich einen Vollaudit
- **Optimal**: Woechentlich, insbesondere nach Aenderungen an der Infrastruktur
- **Nach Massnahmen**: Domain-Audit zur Verifikation nach Behebung von Findings

Geplante Audits koennen unter [Einstellungen > Zeitplaene](../bedienung/einstellungen.md) automatisiert werden.

### Was bedeutet der Confidence-Wert?

Der Confidence-Wert (0-100%) zeigt wie zuverlaessig die automatische Bewertung eines Controls ist:

| Bereich | Bedeutung |
|---------|-----------|
| 80-100% | Hohe Zuverlaessigkeit — Ergebnis kann direkt uebernommen werden |
| 60-79% | Mittlere Zuverlaessigkeit — Stichprobenartige Pruefung empfohlen |
| 0-59% | Geringe Zuverlaessigkeit — Manuelle Ueberpruefung notwendig |

### Was passiert wenn ein Audit unterbrochen wird?

Der Audit laeuft im Hintergrund weiter, auch wenn Sie den Browser-Tab schliessen. Die Ergebnisse finden Sie anschliessend im Audit-Verlauf.

---

## Findings

### Was ist der Unterschied zwischen Major NC und Minor NC?

| Severity | Beschreibung | Beispiel |
|----------|-------------|---------|
| **Major NC** | Fehlende oder nicht wirksame Sicherheitsmassnahme — direktes Risiko | Keine Verschluesselung fuer Daten in Transit |
| **Minor NC** | Massnahme vorhanden aber nicht vollstaendig konform | Passwort-Policy erlaubt 8 statt 12 Zeichen |

### Was bedeutet OFI?

**Opportunity for Improvement** — eine Verbesserungsmoeglichkeit die ueber die Mindestanforderungen hinausgeht. OFIs sind optional umzusetzen, zeigen aber Best Practices auf.

### Kann ich Findings exportieren?

Ja, der Findings-Browser bietet eine **CSV-Export-Funktion**. Der Export beruecksichtigt die aktiven Filter — so koennen Sie zum Beispiel nur offene Major NCs exportieren.

### Wie schliesse ich ein Finding ab?

1. Massnahme umsetzen
2. Status auf "Behoben" setzen
3. Domain-Audit zur Verifikation durchfuehren
4. Status auf "Akzeptiert" setzen

Details: [Remediation](../bedienung/remediation.md)

---

## KI-Integration

### Ist die KI-Integration Pflicht?

Nein. Alle Kernfunktionen arbeiten vollstaendig ohne KI:

- Audits mit regelbasierten Checks
- Findings-Verwaltung und Remediation-Tracking
- Reports und Drift-Detection
- Cross-Standard-Mapping und Matrix-Analytik
- Dokumente hochladen und analysieren

Der Chat-Assistent nutzt vorgefertigte Antworten wenn keine KI verfuegbar ist.

### Welche KI wird verwendet?

Claude von Anthropic. Sie benoetigen eine **Claude Code Subscription** von [claude.ai](https://claude.ai). Die Authentifizierung erfolgt per OAuth direkt im Browser.

### Kann ich eine andere KI verwenden?

Derzeit wird ausschliesslich Claude unterstuetzt. Die Architektur erlaubt grundsaetzlich die Integration weiterer Anbieter in zukuenftigen Versionen.

### Welche Daten werden an Claude gesendet?

| Gesendet | Nicht gesendet |
|----------|---------------|
| Control-Beschreibungen | Hochgeladene Dokumente |
| Gefundene Evidenz (Dateinamen, Configs) | Passwoerter oder Credentials |
| Chat-Nachrichten | Personenbezogene Daten |
| Audit-Anweisungen | Vollstaendige DB-Inhalte |

Details: [Datenschutz](../schnellstart/datenschutz.md)

---

## Mehrsprachigkeit

### Welche Sprachen werden unterstuetzt?

Die Oberflaeche ist auf **Deutsch** und **Englisch** verfuegbar. Die Sprache wird unter [Einstellungen > Praeferenzen](../bedienung/einstellungen.md) gewaehlt.

### In welcher Sprache sind die Standards?

Die Standard-Beschreibungen und AUDIT-CHECKs sind in **Deutsch** hinterlegt. Englische Uebersetzungen sind in der Knowledge-Base verfuegbar.

---

## Sicherheit

### Wie werden meine Daten geschuetzt?

- **Lokale Speicherung**: Alle Daten bleiben auf Ihrem System (SQLite + Dateisystem)
- **Keine Telemetrie**: Keine Nutzungsstatistiken, Crash-Reports oder Analytics
- **OAuth-Tokens**: Gespeichert mit chmod 600, nur fuer den aktuellen Benutzer lesbar
- **Verschluesselung**: Empfohlen auf Dateisystem-Ebene (LUKS, FileVault, BitLocker)

### Kann ich ComplianceOS im Internet erreichbar machen?

ComplianceOS ist fuer den internen Einsatz konzipiert. Wenn Sie es extern erreichbar machen muessen, verwenden Sie einen **Reverse Proxy mit Authentifizierung** (z.B. nginx + Basic Auth oder SSO). Details: [Docker-Konfiguration](../schnellstart/docker.md)
