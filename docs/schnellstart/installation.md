# Installation

## Voraussetzungen

### Pflicht

| Anforderung | Minimum | Empfohlen |
|-------------|---------|-----------|
| **Docker** + **Docker Compose** | v2.0+ | v2.20+ |
| **RAM** | 512 MB | 1 GB |
| **Festplatte** | 1 GB | 5 GB (für Audit-Daten) |
| **Browser** | Chrome 90+ / Firefox 90+ / Safari 15+ / Edge 90+ | Aktuelle Version |
| **Betriebssystem** | Linux, macOS, Windows (mit WSL2) | Linux |

### Optional (für KI-Features)

| Anforderung | Beschreibung |
|-------------|-------------|
| **Claude Code Subscription** | Für KI-Chat, KI-gestützte Audit-Bewertungen und Policy-Generierung |
| **Internetzugang** | Nur für KI-Anfragen an die Claude API (alle anderen Daten bleiben lokal) |

!!! info "Ohne Claude AI"
    ComplianceOS funktioniert auch ohne Claude AI. Die Audit-Engine, Findings, Remediation, Reports und alle anderen Kernfunktionen sind vollständig lokal. Nur der Chat und die KI-gestützten Bewertungen benötigen die Claude-Anbindung.

---

## Installation mit Docker (empfohlen)

### 1. Repository klonen

```bash
git clone https://github.com/silentspike/complianceos.git
cd complianceos
```

### 2. Container starten

```bash
docker compose up -d
```

Docker lädt das Image, erstellt die Datenbank und startet den Server. Der erste Start dauert ca. 30-60 Sekunden.

### 3. Im Browser öffnen

Öffnen Sie [http://localhost:8001](http://localhost:8001). Sie werden auf die **Setup-Seite** weitergeleitet, wenn Claude AI noch nicht konfiguriert ist.

### 4. Health-Check prüfen

```bash
curl http://localhost:8001/api/health
```

Erwartete Antwort:

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "db": true,
  "knowledge": true,
  "claude_sdk": true,
  "disk_free_mb": 43613
}
```

!!! tip "Health-Check Felder"
    - `db`: Datenbankverbindung funktioniert
    - `knowledge`: Wissensbasis (135 Controls, 9 Standards) geladen
    - `claude_sdk`: Claude AI SDK verfügbar (optional)
    - `disk_free_mb`: Freier Speicher in MB

---

## Installation mit pip

Für Entwickler oder Umgebungen ohne Docker:

### 1. Repository klonen

```bash
git clone https://github.com/silentspike/complianceos.git
cd complianceos
```

### 2. Virtual Environment erstellen

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
```

### 3. Abhängigkeiten installieren

```bash
# Basis-Installation
pip install -e .

# Mit KI-Features
pip install -e ".[ai]"

# Mit Dokumenten-Parser (PDF, DOCX, XLSX)
pip install -e ".[docs]"

# Alles zusammen
pip install -e ".[ai,docs]"
```

### 4. Server starten

```bash
make dev
# oder direkt:
python -m uvicorn app.main:app --host 0.0.0.0 --port 8001
```

---

## Port ändern

### Docker

Bearbeiten Sie `docker-compose.yml`:

```yaml
ports:
  - "9000:8001"  # Externer Port : Interner Port
```

Dann neu starten:

```bash
docker compose up -d
```

### pip

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 9000
```

---

## Aktualisieren

### Docker

```bash
cd complianceos
git pull
docker compose pull
docker compose up -d
```

### pip

```bash
cd complianceos
git pull
pip install -e ".[ai,docs]"
```

!!! tip "Datenbank-Migrationen"
    Nach einem Update führt ComplianceOS automatisch Datenbank-Migrationen beim Start durch. Bestehende Daten bleiben erhalten.

---

## Deinstallation

### Container stoppen (Daten bleiben erhalten)

```bash
docker compose down
```

### Container UND Daten löschen

```bash
docker compose down -v
```

!!! danger "Datenverlust"
    `docker compose down -v` löscht alle gespeicherten Daten unwiderruflich: Audit-Ergebnisse, Findings, Dokumente, Policies, Einstellungen und Chat-Verläufe. Erstellen Sie vorher ein Backup der `data/`-Verzeichnisses.

---

## Fehlerbehebung

### Container startet nicht

```bash
# Logs anzeigen
docker compose logs -f complianceos

# Container-Status pruefen
docker compose ps
```

### Port bereits belegt

```
Error: address already in use :::8001
```

Ein anderer Dienst nutzt Port 8001. Ändern Sie den Port (siehe oben) oder stoppen Sie den anderen Dienst.

### Datenbank-Fehler

```bash
# Datenbank-Zustand pruefen
docker compose exec complianceos python -c "
import sqlite3
conn = sqlite3.connect('/app/data/complianceos.db')
print('Tables:', [r[0] for r in conn.execute(\"SELECT name FROM sqlite_master WHERE type='table'\").fetchall()])
"
```

### Kein Internetzugang für Claude AI

ComplianceOS benötigt Internetzugang nur für die Claude API. Wenn kein Internet verfügbar ist, funktionieren alle Kernfunktionen weiterhin — nur Chat und KI-Bewertungen sind deaktiviert.
