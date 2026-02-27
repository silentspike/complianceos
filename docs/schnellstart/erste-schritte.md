# Erste Schritte

Diese Anleitung führt Sie in 5 Schritten vom leeren System zum ersten Audit-Ergebnis.

---

## 1. Projekt anlegen

ComplianceOS arbeitet projektbezogen. Jedes Projekt repräsentiert eine Organisation, ein Team oder einen Audit-Scope.

1. Öffnen Sie **Einstellungen** in der Seitenleiste
2. Scrollen Sie zum Abschnitt **Projekte**
3. Geben Sie einen Projektnamen ein (z.B. "SecureTech Solutions GmbH")
4. Geben Sie den **Projekt-Pfad** ein — das Verzeichnis auf dem Server, das ComplianceOS prüfen soll
5. Klicken Sie auf **Projekt erstellen**

Das neue Projekt wird automatisch aktiv. In der Kopfzeile sehen Sie den Projektnamen als Dropdown — hier können Sie später zwischen Projekten wechseln.

### Was ist der Projekt-Pfad?

Der Projekt-Pfad zeigt auf das Verzeichnis, das Ihre **Infrastruktur-Dateien** enthält. ComplianceOS durchsucht dieses Verzeichnis automatisch nach Konfigurationen, Richtlinien und Sicherheitseinstellungen.

**Ideal geeignete Inhalte:**

- Konfigurationsdateien (nginx.conf, docker-compose.yml, Terraform, Ansible)
- Sicherheitsrichtlinien als Dateien (Passwort-Policy, Backup-Plan, Notfallplan)
- Infrastruktur-Code (Dockerfiles, CI/CD-Pipelines, Helm-Charts)
- Dokumentation (Architektur-Dokumente, Betriebshandbücher)

!!! info "Docker-Benutzer"
    Bei Docker-Installationen ist der Projekt-Pfad ein Pfad **innerhalb** des Containers. Mounten Sie Ihr Projektverzeichnis als Volume in der `docker-compose.yml`:
    ```yaml
    volumes:
      - /pfad/auf/host:/app/mein-projekt
    ```
    Dann verwenden Sie `/app/mein-projekt` als Projekt-Pfad.

Zusätzlich zum Projekt-Pfad können Sie unter **Dokumente** weitere Dateien hochladen (PDF, Word, Excel, Markdown, Text) — zum Beispiel Richtlinien oder Zertifikate die nicht im Projektverzeichnis liegen. Details: [Audits > Was wird geprüft?](../bedienung/audits.md#was-wird-gepruft-quellen-und-evidenz)

<figure class="screenshot" markdown>
![Dashboard nach Projekterstellung](../screenshots/dashboard/dashboard-medidata.png)
<figcaption>Dashboard eines neuen Projekts — noch keine Audits durchgeführt</figcaption>
</figure>

!!! tip "Mehrere Projekte"
    Sie können beliebig viele Projekte anlegen. Jedes Projekt hat eigene Audit-Ergebnisse, Findings und Policies. Der Wechsel erfolgt über das Dropdown in der Kopfzeile.

---

## 2. Ersten Audit starten

1. Klicken Sie auf **Audits** in der Seitenleiste
2. Der **Projekt-Pfad** ist bereits vorausgefüllt
3. Wählen Sie den **Modus**:
   - **Vollständig**: Prüft alle 135 Controls über alle 12 Domains
   - **Domain**: Prüft nur eine bestimmte Domain (z.B. CRYPTO, ACCESS)
4. Klicken Sie auf **Audit starten**

<figure class="screenshot" markdown>
![Audits-Seite](../screenshots/audits/audits-overview.png)
<figcaption>Audit-Seite mit Startformular und Audit-Verlauf</figcaption>
</figure>

!!! info "Audit-Dauer"
    - **Vollaudit**: 1-5 Minuten (abhängig von Systemkomplexität und KI-Verfügbarkeit)
    - **Domain-Audit**: Wenige Sekunden bis 1 Minute
    - Der Fortschritt wird live auf der Seite angezeigt

---

## 3. Ergebnisse verstehen

Nach Abschluss werden Sie automatisch zur Ergebnisseite weitergeleitet:

<figure class="screenshot" markdown>
![Dashboard mit Ergebnissen](../screenshots/dashboard/dashboard-overview.png)
<figcaption>Dashboard nach einem Vollaudit — Compliance-Score, Findings-Verteilung und Domain-Scores</figcaption>
</figure>

### Compliance-Score

Der **Score-Ring** zeigt den Gesamtwert von 0-100%:

| Bereich | Farbe | Bedeutung |
|---------|-------|-----------|
| 80-100% | Grün | Guter Zustand, wenige Abweichungen |
| 60-79% | Gelb | Handlungsbedarf, relevante Lücken |
| 40-59% | Orange | Erheblicher Handlungsbedarf |
| 0-39% | Rot | Kritisch — viele schwerwiegende Abweichungen |

### Severity-Stufen

Jedes Finding wird einer Severity zugeordnet:

| Severity | Badge | Bedeutung |
|----------|-------|-----------|
| **Major NC** | <span class="badge badge--major-nc">MAJOR NC</span> | Schwerwiegende Nichtkonformität — sofortige Massnahme erforderlich |
| **Minor NC** | <span class="badge badge--minor-nc">MINOR NC</span> | Geringfügige Nichtkonformität — Massnahme innerhalb definierter Frist |
| **Observation** | <span class="badge badge--info">OBSERVATION</span> | Beobachtung — potentielles Risiko oder Verbesserungsmöglichkeit |
| **OFI** | <span class="badge badge--ofi">OFI</span> | Opportunity for Improvement — Optimierungsvorschlag |

---

## 4. Findings bearbeiten

1. Klicken Sie auf **Findings** in der Seitenleiste
2. Nutzen Sie die Filter oben um nach Severity, Domain oder Status zu filtern
3. Klicken Sie auf ein Finding für die Detailansicht

<figure class="screenshot" markdown>
![Finding-Detail](../screenshots/findings/finding-detail.png)
<figcaption>Finding-Detail mit Beschreibung, Empfehlung, Evidenz und Reasoning Chain</figcaption>
</figure>

Jedes Finding zeigt:

- **Beschreibung**: Was wurde festgestellt
- **Empfehlung**: Konkrete Handlungsempfehlung
- **Evidenz**: Welche Dateien/Konfigurationen geprüft wurden
- **Reasoning Chain**: Begründungskette der KI-Bewertung
- **Status-Workflow**: Offen → In Arbeit → Behoben → Akzeptiert

Ändern Sie den Status über die Buttons im Remediation-Status-Bereich.

---

## 5. Nächste Schritte

Nach dem ersten Audit empfehlen sich folgende Aktionen:

| Aktion | Seite | Beschreibung |
|--------|-------|-------------|
| Massnahmen planen | [Remediation](../bedienung/remediation.md) | Kanban-Board für Massnahmen-Tracking |
| Richtlinie generieren | [Policies](../bedienung/policies.md) | Fehlende Policies aus Vorlagen erstellen |
| KI-Beratung nutzen | [Chat](../bedienung/chat.md) | Compliance-Fragen im Chat stellen |
| Report erstellen | [Reports](../bedienung/reports.md) | Audit-Bericht für Management oder Auditoren |
| Risiken bewerten | [Executive](../bedienung/executive.md) | Risiko-Matrix und Business Impact |
| Audit planen | [Einstellungen](../bedienung/einstellungen.md) | Automatische Audit-Zeitpläne einrichten |

!!! tip "Regelmässige Audits"
    Führen Sie regelmässig Audits durch (z.B. monatlich). ComplianceOS erkennt automatisch **Drift** — Veränderungen gegenüber dem vorherigen Audit. So sehen Sie sofort ob sich Ihr Compliance-Zustand verbessert oder verschlechtert hat.
