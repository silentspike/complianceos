# FAQ

Häufig gestellte Fragen zu ComplianceOS — sortiert nach Themenbereichen.

---

## Allgemein

### Was ist ComplianceOS?

ComplianceOS ist eine On-Premise-Plattform für automatisierte Compliance-Audits. Sie prüft Ihre IT-Infrastruktur gegen 9 internationale Standards (ISO 27001, NIS2, BSI IT-Grundschutz und weitere) und hilft bei der Identifikation und Behebung von Abweichungen.

### Für wen ist ComplianceOS gedacht?

ComplianceOS richtet sich an:

- **Compliance-Beauftragte** die regelmässig interne Audits durchführen
- **CISOs und IT-Sicherheitsverantwortliche** die den Compliance-Zustand überwachen
- **Geschäftsführung** die einen Überblick über Risiken und Compliance-Stand benötigt
- **IT-Teams** die Sicherheitsmassnahmen umsetzen und nachverfolgen

### Ersetzt ComplianceOS einen externen Auditor?

Nein. ComplianceOS ist ein Werkzeug zur Vorbereitung und Durchführung **interner Audits**. Für offizielle Zertifizierungen (z.B. ISO 27001) benötigen Sie weiterhin einen akkreditierten externen Auditor. ComplianceOS hilft Ihnen jedoch, optimal auf ein externes Audit vorbereitet zu sein.

### Welche Daten verlassen mein System?

- **Ohne KI-Integration**: Keine Daten verlassen Ihr System
- **Mit KI-Integration**: Audit-Prüfpunkte und Chat-Nachrichten werden an die Claude API (Anthropic) gesendet
- **Nie gesendet**: Hochgeladene Dokumente, Passwort-Richtlinien, personenbezogene Daten, OAuth-Tokens

Details: [Datenschutz](../schnellstart/datenschutz.md)

### Ist ComplianceOS kostenlos?

ComplianceOS ist unter der Apache-2.0-Lizenz frei verfügbar. Die optionale KI-Integration erfordert eine Claude Code Subscription von Anthropic.

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

Docker ist die empfohlene Methode für den produktiven Einsatz. Details: [Installation](../schnellstart/installation.md)

### Wie aktualisiere ich auf eine neue Version?

```bash
cd complianceos
git pull
docker compose build
docker compose up -d
```

Datenbank-Migrationen werden automatisch beim Start durchgeführt. Bestehende Daten bleiben erhalten.

### Wie erstelle ich ein Backup?

```bash
docker run --rm \
  -v complianceos_complianceos-data:/data \
  -v $(pwd):/backup \
  busybox tar czf /backup/complianceos-backup-$(date +%Y%m%d).tar.gz /data
```

Details: [Docker-Konfiguration](../schnellstart/docker.md)

### Kann ich den Port ändern?

Ja, in der `docker-compose.yml`:

```yaml
ports:
  - "9000:8001"  # Externer Port 9000
```

---

## Audits

### Wie lange dauert ein Vollaudit?

Abhängig von der Systemleistung und KI-Verfügbarkeit:

- **Vollaudit**: 1-5 Minuten für alle 135 Controls
- **Domain-Audit**: 10-60 Sekunden

### Kann ich nur einen Teilbereich prüfen?

Ja, wählen Sie beim Audit-Start den Modus **Domain-Audit** und eine der 12 Domains (z.B. CRYPTO, ACCESS, BACKUP). So prüfen Sie gezielt einen einzelnen Sicherheitsbereich.

### Wie oft sollte ich Audits durchführen?

- **Empfohlen**: Mindestens monatlich einen Vollaudit
- **Optimal**: Wöchentlich, insbesondere nach Änderungen an der Infrastruktur
- **Nach Massnahmen**: Domain-Audit zur Verifikation nach Behebung von Findings

Geplante Audits können unter [Einstellungen > Zeitpläne](../bedienung/einstellungen.md) automatisiert werden.

### Was bedeutet der Confidence-Wert?

Der Confidence-Wert (0-100%) zeigt wie zuverlässig die automatische Bewertung eines Controls ist:

| Bereich | Bedeutung |
|---------|-----------|
| 80-100% | Hohe Zuverlässigkeit — Ergebnis kann direkt übernommen werden |
| 60-79% | Mittlere Zuverlässigkeit — Stichprobenartige Prüfung empfohlen |
| 0-59% | Geringe Zuverlässigkeit — Manuelle Überprüfung notwendig |

### Was passiert wenn ein Audit unterbrochen wird?

Der Audit läuft im Hintergrund weiter, auch wenn Sie den Browser-Tab schliessen. Die Ergebnisse finden Sie anschliessend im Audit-Verlauf.

### Woher kommen die 2.042 AUDIT-CHECKs?

Die AUDIT-CHECKs sind das Ergebnis einer systematischen Analyse aller 9 Standards. Jeder Artikel, jede Klausel und jeder Baustein wurde in atomare, technisch prüfbare Anforderungen zerlegt. Beispiel: Ein einzelner ISO-Control wie "Kryptografie" (A.8.24) wird in 5-15 konkrete Prüffragen aufgelöst (TLS-Version, Algorithmen, Schlüsselmanagement etc.).

Die Knowledge Base wird mit dem Quellcode ausgeliefert und beim Start geladen — keine externe Datenbank oder Internetverbindung erforderlich. Eine detaillierte Erklärung finden Sie unter [Audits > Wie funktioniert die Audit-Engine?](../bedienung/audits.md#wie-funktioniert-die-audit-engine).

### Wie unterscheidet sich ein automatisierter von einem manuellen Check?

| Methode | Vorgehen | Beispiel | Confidence |
|---------|----------|---------|------------|
| **Automated** (71 Controls) | Pattern-Matching in Dateien, Konfigurationsvergleiche, Dateiexistenz | TLS >= 1.2? Passwort-Policy vorhanden? | 60-95% |
| **Hybrid** (11 Controls) | Automatischer Check plus Interview-Fragen | Backup vorhanden? + Recovery-Tests dokumentiert? | 40-85% |
| **Manual** (53 Controls) | Dokumenten-Review, Prozessbewertung | Notfallplan aktuell? Schulungen durchgeführt? | 20-80% |

Die Confidence-Werte steigen deutlich wenn Claude AI für die Bewertung verfügbar ist, insbesondere bei Hybrid- und Manual-Checks.

### Kann ich eigene Controls oder Checks hinzufügen?

Die Control-Matrix ist in der Datei `control-matrix.yaml` definiert. Erfahrene Benutzer können dort eigene Controls ergänzen oder bestehende anpassen. ComplianceOS lädt die Matrix beim Start neu.

---

## Findings

### Was ist der Unterschied zwischen Major NC und Minor NC?

| Severity | Beschreibung | Beispiel |
|----------|-------------|---------|
| **Major NC** | Fehlende oder nicht wirksame Sicherheitsmassnahme — direktes Risiko | Keine Verschlüsselung für Daten in Transit |
| **Minor NC** | Massnahme vorhanden aber nicht vollständig konform | Passwort-Policy erlaubt 8 statt 12 Zeichen |

### Was bedeutet OFI?

**Opportunity for Improvement** — eine Verbesserungsmöglichkeit die über die Mindestanforderungen hinausgeht. OFIs sind optional umzusetzen, zeigen aber Best Practices auf.

### Kann ich Findings exportieren?

Ja, der Findings-Browser bietet eine **CSV-Export-Funktion**. Der Export berücksichtigt die aktiven Filter — so können Sie zum Beispiel nur offene Major NCs exportieren.

### Wie schliesse ich ein Finding ab?

1. Massnahme umsetzen
2. Status auf "Behoben" setzen
3. Domain-Audit zur Verifikation durchführen
4. Status auf "Akzeptiert" setzen

Details: [Remediation](../bedienung/remediation.md)

---

## KI-Integration

### Ist die KI-Integration Pflicht?

Nein. Alle Kernfunktionen arbeiten vollständig ohne KI:

- Audits mit regelbasierten Checks
- Findings-Verwaltung und Remediation-Tracking
- Reports und Drift-Detection
- Cross-Standard-Mapping und Matrix-Analytik
- Dokumente hochladen und analysieren

Der Chat-Assistent nutzt vorgefertigte Antworten wenn keine KI verfügbar ist.

### Welche KI wird verwendet?

Claude von Anthropic. Sie benötigen eine **Claude Code Subscription** von [claude.ai](https://claude.ai). Die Authentifizierung erfolgt per OAuth direkt im Browser.

### Kann ich eine andere KI verwenden?

Derzeit wird ausschliesslich Claude unterstützt. Die Architektur erlaubt grundsätzlich die Integration weiterer Anbieter in zukünftigen Versionen.

### Welche Daten werden an Claude gesendet?

| Gesendet | Nicht gesendet |
|----------|---------------|
| Control-Beschreibungen | Hochgeladene Dokumente |
| Gefundene Evidenz (Dateinamen, Configs) | Passwörter oder Credentials |
| Chat-Nachrichten | Personenbezogene Daten |
| Audit-Anweisungen | Vollständige DB-Inhalte |

Details: [Datenschutz](../schnellstart/datenschutz.md)

---

## Mehrsprachigkeit

### Welche Sprachen werden unterstützt?

Die Oberfläche ist auf **Deutsch** und **Englisch** verfügbar. Die Sprache wird unter [Einstellungen > Präferenzen](../bedienung/einstellungen.md) gewählt.

### In welcher Sprache sind die Standards?

Die Standard-Beschreibungen und AUDIT-CHECKs sind in **Deutsch** hinterlegt. Englische Übersetzungen sind in der Knowledge-Base verfügbar.

---

## Sicherheit

### Wie werden meine Daten geschützt?

- **Lokale Speicherung**: Alle Daten bleiben auf Ihrem System (SQLite + Dateisystem)
- **Keine Telemetrie**: Keine Nutzungsstatistiken, Crash-Reports oder Analytics
- **OAuth-Tokens**: Gespeichert mit chmod 600, nur für den aktuellen Benutzer lesbar
- **Verschlüsselung**: Empfohlen auf Dateisystem-Ebene (LUKS, FileVault, BitLocker)

### Kann ich ComplianceOS im Internet erreichbar machen?

ComplianceOS ist für den internen Einsatz konzipiert. Wenn Sie es extern erreichbar machen müssen, verwenden Sie einen **Reverse Proxy mit Authentifizierung** (z.B. nginx + Basic Auth oder SSO). Details: [Docker-Konfiguration](../schnellstart/docker.md)
