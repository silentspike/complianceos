# Einstellungen

Unter Einstellungen verwalten Sie Projekte, Praeferenzen, Team-Mitglieder, geplante Audits, Benachrichtigungen und Feature-Flags.

<figure class="screenshot" markdown>
![Einstellungen](../screenshots/einstellungen/einstellungen-overview.png)
<figcaption>Einstellungen: Praeferenzen, Projekte, Team, Zeitplaene, ntfy-Benachrichtigungen, System-Info und Feature-Flags</figcaption>
</figure>

---

## Praeferenzen

### Sprache

ComplianceOS unterstuetzt zwei Sprachen:

| Sprache | Code | Beschreibung |
|---------|------|-------------|
| **Deutsch** | `de` | Standard — alle Oberflaechen-Texte auf Deutsch |
| **Englisch** | `en` | Alternative — Oberflaeche auf Englisch |

Die Sprache beeinflusst die Oberflaeche, Reports und Chat-Antworten.

### Rolle

Die Rolle bestimmt die Standard-Ansicht im Dashboard:

| Rolle | Dashboard-Ansicht | Beschreibung |
|-------|------------------|-------------|
| **Compliance** | Vollstaendiges technisches Dashboard | Fuer Compliance-Beauftragte |
| **CISO** | Technisches Dashboard + Risiko-Sidebar | Fuer IT-Sicherheitsverantwortliche |
| **Management** | Komprimiertes Executive-Dashboard | Fuer Geschaeftsfuehrung |

Die Rolle kann jederzeit geaendert werden. Im Dashboard-Header koennen Sie auch direkt zwischen den Ansichten wechseln.

---

## Projekte

ComplianceOS arbeitet projektbezogen. Jedes Projekt repraesentiert eine Organisation, ein Team oder einen Audit-Scope.

### Neues Projekt anlegen

1. Scrollen Sie zum Bereich **Projekte**
2. Geben Sie den **Projektnamen** ein (z.B. "SecureTech Solutions GmbH")
3. Geben Sie den **Pfad** zum zu pruefenden Projekt-Verzeichnis ein
4. Klicken Sie auf **Projekt erstellen**

Das neue Projekt wird automatisch aktiv und erscheint im Dropdown oben rechts.

### Projekt wechseln

Klicken Sie oben rechts in der Kopfzeile auf den **Projektnamen** und waehlen Sie ein anderes Projekt aus dem Dropdown. Alle Ansichten (Dashboard, Findings, Audits, etc.) wechseln sofort zum ausgewaehlten Projekt.

### Projekt-Isolation

Jedes Projekt hat vollstaendig eigene Daten:

| Daten | Beschreibung |
|-------|-------------|
| **Audit-Laeufe** | Eigene Audit-Historie und Ergebnisse |
| **Findings** | Eigene Findings mit Status und Remediation |
| **Chat-Sessions** | Eigene Konversationen |
| **Dokumente** | Eigene hochgeladene Dateien |
| **Policies** | Eigene generierte Richtlinien |
| **Reports** | Eigene Audit-Reports und Drift-Detection |
| **Risikobewertungen** | Eigene Risk Assessments |
| **Remediation** | Eigene Massnahmen und Zuweisungen |

!!! tip "Mehrere Projekte"
    Nutzen Sie separate Projekte fuer verschiedene Organisationen, Abteilungen oder Audit-Scopes. So bleiben die Daten sauber getrennt und Sie koennen gezielt pro Projekt berichten.

---

## Team-Mitglieder

Legen Sie Mitarbeiter an die als Verantwortliche fuer Remediation-Aufgaben zugewiesen werden koennen:

| Feld | Pflicht | Beschreibung |
|------|---------|-------------|
| **Name** | Ja | Anzeigename im System |
| **E-Mail** | Nein | Fuer Benachrichtigungen |
| **Rolle** | Nein | compliance, ciso oder management |

Team-Mitglieder stehen dann im Dropdown "Verantwortlich" bei jedem Finding zur Verfuegung.

---

## Geplante Audits (Zeitplaene)

Richten Sie automatische Audit-Laeufe ein die ohne manuellen Eingriff ausfuehren:

### Zeitplan erstellen

1. Scrollen Sie zum Bereich **Geplante Audits**
2. Klicken Sie auf **Neuer Zeitplan**
3. Konfigurieren Sie:

| Feld | Optionen | Beschreibung |
|------|----------|-------------|
| **Modus** | Vollaudit / Domain | Welcher Audit-Typ ausgefuehrt wird |
| **Domain** | ACCESS, BACKUP, etc. | Nur bei Domain-Modus |
| **Intervall** | Taeglich / Woechentlich / Monatlich | Ausfuehrungsfrequenz |
| **Tag** | Montag-Sonntag / 1-28 | Bei woechentlich/monatlich |
| **Uhrzeit** | 00:00-23:59 | Startzeitpunkt |

4. Klicken Sie auf **Aktivieren**

### Zeitplan verwalten

Bestehende Zeitplaene koennen:

- **Aktiviert/Deaktiviert** werden (Toggle-Schalter)
- **Bearbeitet** werden (Intervall, Modus aendern)
- **Geloescht** werden

!!! warning "Container muss laufen"
    Geplante Audits funktionieren nur solange der ComplianceOS-Container laeuft. Stellen Sie sicher dass `restart: unless-stopped` in der `docker-compose.yml` gesetzt ist.

---

## ntfy-Benachrichtigungen

ComplianceOS kann Push-Benachrichtigungen ueber [ntfy](https://ntfy.sh) senden — an Ihr Smartphone, Ihren Desktop oder andere Endgeraete.

### ntfy einrichten

1. Scrollen Sie zum Bereich **Benachrichtigungen**
2. Geben Sie die **ntfy Server-URL** ein (z.B. `https://ntfy.sh` oder Ihr eigener Server)
3. Geben Sie das **Topic** ein (z.B. `complianceos-alerts`)
4. Klicken Sie auf **Speichern**
5. Klicken Sie auf **Test senden** um die Verbindung zu pruefen

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
| **Authentifiziert und einsatzbereit** | Gruen | Claude AI ist verbunden und funktionsfaehig |
| **CLI installiert, nicht authentifiziert** | Gelb | Claude CLI vorhanden, aber kein Token |
| **CLI nicht gefunden** | Rot | Claude CLI nicht installiert |

Bei Problemen mit der Authentifizierung navigieren Sie zu `/setup` um den OAuth-Flow erneut durchzufuehren (siehe [Setup](../schnellstart/setup.md)).

---

## System-Info

Zeigt technische Informationen ueber die ComplianceOS-Installation:

| Information | Beschreibung |
|-------------|-------------|
| **Version** | Aktuell installierte ComplianceOS-Version |
| **Python-Version** | Python-Runtime-Version |
| **Datenbankgroesse** | Aktuelle Groesse der SQLite-Datenbank |
| **Standards** | Anzahl der geladenen Standards (9) |
| **Controls** | Anzahl technischer Pruefpunkte (135) |
| **AUDIT-CHECKs** | Anzahl semantischer Anforderungen (2.042) |
| **Domains** | Anzahl Sicherheitsbereiche (12) |

---

## Feature-Flags

Feature-Flags steuern welche optionalen Funktionen aktiviert sind:

| Flag | Standard | Beschreibung |
|------|----------|-------------|
| **teammates** | `false` | KI-Agent-Orchestrierung fuer parallele Audit-Bewertung |
| **policy_gen** | `true` | KI-gestuetzte Policy-Generierung |
| **pdf_upload** | `true` | PDF-Dokument-Upload und -Analyse |
| **dsgvo** | `true` | DSGVO-Standard in Audits einbeziehen |

Feature-Flags koennen hier per Toggle umgeschaltet werden. Die Aenderung wird sofort wirksam.

!!! info "Umgebungsvariablen"
    Feature-Flags koennen auch per Umgebungsvariable gesetzt werden (z.B. `ENABLE_TEAMMATES=true` in der `docker-compose.yml`). Die Umgebungsvariable setzt den Initialwert — Aenderungen ueber die Oberflaeche haben Vorrang.
