# Docker-Konfiguration

## docker-compose.yml

Die Standard-Konfiguration:

```yaml
services:
  complianceos:
    image: ghcr.io/obtfusi/complianceos:latest
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

## Umgebungsvariablen

| Variable | Standard | Beschreibung |
|----------|----------|-------------|
| `COMPLIANCEOS_PORT` | `8001` | Interner Server-Port |
| `COMPLIANCEOS_LOG_LEVEL` | `INFO` | Log-Level (DEBUG, INFO, WARNING, ERROR) |
| `COMPLIANCEOS_LANG` | `de` | Oberflaechen-Sprache |
| `ENABLE_TEAMMATES` | `false` | KI-Agent-Orchestrierung aktivieren |
| `ENABLE_PDF_UPLOAD` | `true` | PDF-Upload ermoeglichen |
| `ENABLE_POLICY_GEN` | `true` | Policy-Generierung aktivieren |
| `ENABLE_DSGVO` | `true` | DSGVO-Standard einbeziehen |

## Daten-Volume

Alle Daten (Datenbank, Audit-Ergebnisse, hochgeladene Dokumente) werden im Docker Volume `complianceos-data` gespeichert.

### Backup

```bash
# Volume-Inhalt sichern
docker run --rm -v complianceos-data:/data -v $(pwd):/backup \
  busybox tar czf /backup/complianceos-backup.tar.gz /data
```

### Restore

```bash
# Volume-Inhalt wiederherstellen
docker run --rm -v complianceos-data:/data -v $(pwd):/backup \
  busybox tar xzf /backup/complianceos-backup.tar.gz -C /
```

## Logs ansehen

```bash
# Live-Logs
docker compose logs -f

# Letzte 100 Zeilen
docker compose logs --tail 100
```

## Ressourcen begrenzen

```yaml
services:
  complianceos:
    # ...
    deploy:
      resources:
        limits:
          memory: 1G
          cpus: "2.0"
```

## Hinter Reverse Proxy (nginx)

```nginx
server {
    listen 443 ssl;
    server_name compliance.ihre-domain.de;

    location / {
        proxy_pass http://localhost:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
