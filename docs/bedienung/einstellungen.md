# Einstellungen

Unter Einstellungen verwalten Sie Projekte, Präferenzen, Team-Mitglieder, geplante Audits, Benachrichtigungen und Feature-Flags.

<figure class="screenshot" markdown>
![Einstellungen](../screenshots/einstellungen/einstellungen-overview.png)
<figcaption>Einstellungen: Präferenzen, Projekte, Team, Zeitpläne, ntfy-Benachrichtigungen, System-Info und Feature-Flags</figcaption>
</figure>

---

## Präferenzen

### Sprache

ComplianceOS unterstützt zwei Sprachen:

| Sprache | Code | Beschreibung |
|---------|------|-------------|
| **Deutsch** | `de` | Standard — alle Oberflächen-Texte auf Deutsch |
| **Englisch** | `en` | Alternative — Oberfläche auf Englisch |

Die Sprache beeinflusst die Oberfläche, Reports und Chat-Antworten.

### Rolle

Die Rolle bestimmt die Standard-Ansicht im Dashboard:

| Rolle | Dashboard-Ansicht | Beschreibung |
|-------|------------------|-------------|
| **Compliance** | Vollständiges technisches Dashboard | Für Compliance-Beauftragte |
| **CISO** | Technisches Dashboard + Risiko-Sidebar | Für IT-Sicherheitsverantwortliche |
| **Management** | Komprimiertes Executive-Dashboard | Für Geschäftsführung |

Die Rolle kann jederzeit geändert werden. Im Dashboard-Header können Sie auch direkt zwischen den Ansichten wechseln.

---

## Projekte

ComplianceOS arbeitet projektbezogen. Jedes Projekt repräsentiert eine Organisation, ein Team oder einen Audit-Scope.

### Neues Projekt anlegen

1. Scrollen Sie zum Bereich **Projekte**
2. Geben Sie den **Projektnamen** ein (z.B. "SecureTech Solutions GmbH")
3. Geben Sie den **Pfad** zum zu prüfenden Projekt-Verzeichnis ein
4. Klicken Sie auf **Projekt erstellen**

Das neue Projekt wird automatisch aktiv und erscheint im Dropdown oben rechts.

### Projekt wechseln

Klicken Sie oben rechts in der Kopfzeile auf den **Projektnamen** und wählen Sie ein anderes Projekt aus dem Dropdown. Alle Ansichten (Dashboard, Findings, Audits, etc.) wechseln sofort zum ausgewählten Projekt.

### Projekt-Isolation

Jedes Projekt hat vollständig eigene Daten:

| Daten | Beschreibung |
|-------|-------------|
| **Audit-Läufe** | Eigene Audit-Historie und Ergebnisse |
| **Findings** | Eigene Findings mit Status und Remediation |
| **Chat-Sessions** | Eigene Konversationen |
| **Dokumente** | Eigene hochgeladene Dateien |
| **Policies** | Eigene generierte Richtlinien |
| **Reports** | Eigene Audit-Reports und Drift-Detection |
| **Risikobewertungen** | Eigene Risk Assessments |
| **Remediation** | Eigene Massnahmen und Zuweisungen |

!!! tip "Mehrere Projekte"
    Nutzen Sie separate Projekte für verschiedene Organisationen, Abteilungen oder Audit-Scopes. So bleiben die Daten sauber getrennt und Sie können gezielt pro Projekt berichten.

---

## Team-Mitglieder

Legen Sie Mitarbeiter an die als Verantwortliche für Remediation-Aufgaben zugewiesen werden können:

| Feld | Pflicht | Beschreibung |
|------|---------|-------------|
| **Name** | Ja | Anzeigename im System |
| **E-Mail** | Nein | Für Benachrichtigungen |
| **Rolle** | Nein | compliance, ciso oder management |

Team-Mitglieder stehen dann im Dropdown "Verantwortlich" bei jedem Finding zur Verfügung.

---

## Geplante Audits (Zeitpläne)

Richten Sie automatische Audit-Läufe ein die ohne manuellen Eingriff ausführen:

### Zeitplan erstellen

1. Scrollen Sie zum Bereich **Geplante Audits**
2. Klicken Sie auf **Neuer Zeitplan**
3. Konfigurieren Sie:

| Feld | Optionen | Beschreibung |
|------|----------|-------------|
| **Modus** | Vollaudit / Domain | Welcher Audit-Typ ausgeführt wird |
| **Domain** | ACCESS, BACKUP, etc. | Nur bei Domain-Modus |
| **Intervall** | Täglich / Wöchentlich / Monatlich | Ausfuehrungsfrequenz |
| **Tag** | Montag-Sonntag / 1-28 | Bei wöchentlich/monatlich |
| **Uhrzeit** | 00:00-23:59 | Startzeitpunkt |

4. Klicken Sie auf **Aktivieren**

### Zeitplan verwalten

Bestehende Zeitpläne können:

- **Aktiviert/Deaktiviert** werden (Toggle-Schalter)
- **Bearbeitet** werden (Intervall, Modus ändern)
- **Gelöscht** werden

!!! warning "Container muss laufen"
    Geplante Audits funktionieren nur solange der ComplianceOS-Container läuft. Stellen Sie sicher dass `restart: unless-stopped` in der `docker-compose.yml` gesetzt ist.

---

## ntfy-Benachrichtigungen

ComplianceOS kann Push-Benachrichtigungen über [ntfy](https://ntfy.sh) senden — an Ihr Smartphone, Ihren Desktop oder andere Endgeräte.

### ntfy einrichten

1. Scrollen Sie zum Bereich **Benachrichtigungen**
2. Geben Sie die **ntfy Server-URL** ein (z.B. `https://ntfy.sh` oder Ihr eigener Server)
3. Geben Sie das **Topic** ein (z.B. `complianceos-alerts`)
4. Klicken Sie auf **Speichern**
5. Klicken Sie auf **Test senden** um die Verbindung zu prüfen

### Benachrichtigungen erhalten bei

- **Audit abgeschlossen**: Nach jedem geplanten oder manuellen Audit
- **Neue Major NCs**: Wenn ein Audit neue schwerwiegende Findings identifiziert
- **Deadline-Warnung**: Wenn eine Remediation-Deadline naht

!!! tip "ntfy-App"
    Installieren Sie die ntfy-App auf Ihrem Smartphone (Android/iOS) und abonnieren Sie Ihr Topic. So erhalten Sie Push-Benachrichtigungen in Echtzeit.

---

## Claude AI Status

Der Bereich **Claude AI** zeigt den aktuellen Verbindungsstatus:

| Status | Farbe | Bedeutung |
|--------|-------|-----------|
| **Authentifiziert und einsatzbereit** | Grün | Claude AI ist verbunden und funktionsfähig |
| **CLI installiert, nicht authentifiziert** | Gelb | Claude CLI vorhanden, aber kein Token |
| **CLI nicht gefunden** | Rot | Claude CLI nicht installiert |

Bei Problemen mit der Authentifizierung navigieren Sie zu `/setup` um den OAuth-Flow erneut durchzuführen (siehe [Setup](../schnellstart/setup.md)).

---

## System-Info

Zeigt technische Informationen über die ComplianceOS-Installation:

| Information | Beschreibung |
|-------------|-------------|
| **Version** | Aktuell installierte ComplianceOS-Version |
| **Python-Version** | Python-Runtime-Version |
| **Datenbankgrösse** | Aktuelle Grösse der SQLite-Datenbank |
| **Standards** | Anzahl der geladenen Standards (9) |
| **Controls** | Anzahl technischer Prüfpunkte (135) |
| **AUDIT-CHECKs** | Anzahl semantischer Anforderungen (2.042) |
| **Domains** | Anzahl Sicherheitsbereiche (12) |

---

## Feature-Flags

Feature-Flags steuern welche optionalen Funktionen aktiviert sind:

| Flag | Standard | Beschreibung |
|------|----------|-------------|
| **teammates** | `false` | KI-Agent-Orchestrierung für parallele Audit-Bewertung |
| **policy_gen** | `true` | KI-gestützte Policy-Generierung |
| **pdf_upload** | `true` | PDF-Dokument-Upload und -Analyse |
| **dsgvo** | `true` | DSGVO-Standard in Audits einbeziehen |

Feature-Flags können hier per Toggle umgeschaltet werden. Die Änderung wird sofort wirksam.

!!! info "Umgebungsvariablen"
    Feature-Flags können auch per Umgebungsvariable gesetzt werden (z.B. `ENABLE_TEAMMATES=true` in der `docker-compose.yml`). Die Umgebungsvariable setzt den Initialwert — Änderungen über die Oberfläche haben Vorrang.
