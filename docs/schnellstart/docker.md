# Docker-Konfiguration

ComplianceOS wird als Multi-Stage Docker-Image ausgeliefert. Die empfohlene Methode ist Docker Compose.

---

## docker-compose.yml

Die Standard-Konfiguration:

```yaml
services:
  complianceos:
    build: .
    ports:
      - "8001:8001"
    volumes:
      - complianceos-data:/app/data
    environment:
      - COMPLIANCEOS_LOG_LEVEL=INFO
      - COMPLIANCEOS_LANG=de
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8001/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped

volumes:
  complianceos-data:
```

---

## Umgebungsvariablen

| Variable | Standard | Beschreibung |
|----------|----------|-------------|
| `COMPLIANCEOS_PORT` | `8001` | Interner Server-Port |
| `COMPLIANCEOS_LOG_LEVEL` | `INFO` | Log-Level (`DEBUG`, `INFO`, `WARNING`, `ERROR`) |
| `COMPLIANCEOS_LANG` | `de` | Oberflächen-Sprache (`de` oder `en`) |
| `DATABASE_URL` | `sqlite:///data/complianceos.db` | Datenbank-Pfad |
| `ENABLE_TEAMMATES` | `false` | KI-Agent-Orchestrierung (parallele Audit-Execution) |
| `ENABLE_PDF_UPLOAD` | `true` | PDF-Dokument-Upload |
| `ENABLE_POLICY_GEN` | `true` | Policy-Generierung aus Vorlagen |
| `ENABLE_DSGVO` | `true` | DSGVO-Standard einbeziehen |

!!! tip "Feature Flags"
    Alle `ENABLE_*`-Variablen können auch über die **Einstellungen** im Browser gesteuert werden. Die Umgebungsvariablen setzen den Initialwert.

---

## Daten-Volume

Alle persistenten Daten werden im Docker Volume `complianceos-data` gespeichert:

| Pfad (im Container) | Inhalt |
|---------------------|--------|
| `/app/data/complianceos.db` | SQLite-Datenbank (Audits, Findings, Policies, etc.) |
| `/app/data/uploads/` | Hochgeladene Dokumente |
| `/app/data/exports/` | Generierte PDF-Exporte |

### Backup erstellen

```bash
# Volume-Inhalt als tar.gz sichern
docker run --rm \
  -v complianceos_complianceos-data:/data \
  -v $(pwd):/backup \
  busybox tar czf /backup/complianceos-backup-$(date +%Y%m%d).tar.gz /data
```

### Backup wiederherstellen

```bash
# Container stoppen
docker compose down

# Volume-Inhalt wiederherstellen
docker run --rm \
  -v complianceos_complianceos-data:/data \
  -v $(pwd):/backup \
  busybox tar xzf /backup/complianceos-backup-20260227.tar.gz -C /

# Container starten
docker compose up -d
```

!!! warning "Container stoppen"
    Stoppen Sie den Container immer vor einem Restore, um Datenbankkorruption zu vermeiden.

---

## Logs

```bash
# Live-Logs verfolgen
docker compose logs -f complianceos

# Letzte 100 Zeilen
docker compose logs --tail 100 complianceos

# Nur Fehler anzeigen
docker compose logs complianceos 2>&1 | grep ERROR
```

ComplianceOS nutzt strukturiertes JSON-Logging (structlog), optimiert für Log-Aggregation mit Loki, Elasticsearch oder ähnlichen Systemen.

---

## Ressourcen begrenzen

```yaml
services:
  complianceos:
    deploy:
      resources:
        limits:
          memory: 1G
          cpus: "2.0"
        reservations:
          memory: 256M
          cpus: "0.5"
```

| Ressource | Minimum | Empfohlen | Beschreibung |
|-----------|---------|-----------|-------------|
| RAM | 256 MB | 512 MB - 1 GB | Abhängig von Audit-Grösse und gleichzeitigen Nutzern |
| CPU | 0.5 Cores | 2 Cores | Audit-Execution ist CPU-intensiv |
| Disk | 100 MB | 1-5 GB | Abhängig von Dokumenten-Uploads und Audit-Historie |

---

## Netzwerk-Konfiguration

### Anderen Port verwenden

```yaml
ports:
  - "9000:8001"  # Externer Port 9000 → Interner Port 8001
```

### Nur lokal erreichbar

```yaml
ports:
  - "127.0.0.1:8001:8001"  # Nur von localhost erreichbar
```

### Hinter Reverse Proxy (nginx)

```nginx
server {
    listen 443 ssl;
    server_name compliance.ihre-domain.de;

    ssl_certificate /etc/letsencrypt/live/compliance.ihre-domain.de/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/compliance.ihre-domain.de/privkey.pem;

    location / {
        proxy_pass http://localhost:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # SSE (Server-Sent Events) fuer Live-Fortschritt
        proxy_buffering off;
        proxy_cache off;
        proxy_read_timeout 86400s;
    }
}
```

!!! warning "SSE-Unterstützung"
    Wenn Sie einen Reverse Proxy verwenden, deaktivieren Sie `proxy_buffering` für die korrekte Funktion der Live-Fortschrittsanzeige bei Audits.

---

## Upgrade

```bash
cd complianceos
git pull
docker compose build
docker compose up -d
```

ComplianceOS führt Datenbank-Migrationen automatisch beim Start durch. Bestehende Daten bleiben erhalten.

---

## Fehlerbehebung

### Container startet nicht

```bash
# Detaillierte Logs
docker compose logs complianceos

# Container-Status
docker compose ps

# In laufenden Container einsteigen
docker compose exec complianceos bash
```

### Health-Check schlägt fehl

```bash
# Manueller Health-Check
docker compose exec complianceos curl -f http://localhost:8001/api/health
```

### Datenbank-Probleme

```bash
# Datenbank-Integritaet pruefen
docker compose exec complianceos python3 -c "
import sqlite3
conn = sqlite3.connect('/app/data/complianceos.db')
result = conn.execute('PRAGMA integrity_check').fetchone()
print('DB Status:', result[0])
tables = conn.execute(\"SELECT name FROM sqlite_master WHERE type='table'\").fetchall()
print('Tabellen:', [t[0] for t in tables])
"
```
