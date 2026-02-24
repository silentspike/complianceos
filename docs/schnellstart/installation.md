# Installation

## Voraussetzungen

- **Docker** und **Docker Compose** (v2+)
- Mindestens 512 MB freier RAM
- Mindestens 1 GB Festplatte
- Ein moderner Webbrowser (Chrome, Firefox, Safari, Edge)

Optional fuer KI-Features:

- [Claude Code](https://claude.ai/claude-code) Subscription
- Internetzugang (nur fuer KI-Anfragen)

## Installation mit Docker

```bash
# Repository klonen
git clone https://github.com/silentspike/complianceos.git
cd complianceos

# Starten
docker compose up -d
```

ComplianceOS ist jetzt unter [http://localhost:8001](http://localhost:8001) erreichbar.

## Health Check pruefen

```bash
curl http://localhost:8001/api/health
```

Erwartete Antwort:
```json
{"status": "healthy", "version": "1.0.0", "db": true, "knowledge": true}
```

## Port aendern

Bearbeiten Sie `docker-compose.yml`:

```yaml
ports:
  - "9000:8001"  # Externer Port : Interner Port
```

Dann `docker compose up -d` erneut ausfuehren.

## Aktualisieren

```bash
docker compose pull
docker compose up -d
```

## Deinstallation

```bash
# Container stoppen und entfernen
docker compose down

# Daten ebenfalls loeschen (ACHTUNG: unwiderruflich!)
docker compose down -v
```

!!! warning "Datenverlust"
    Der Befehl `docker compose down -v` loescht alle gespeicherten Daten
    (Audit-Ergebnisse, Findings, Dokumente, Einstellungen).
