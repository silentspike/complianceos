# Dokumente

Laden Sie bestehende Compliance-Dokumente hoch, um sie automatisch analysieren und mit Controls abgleichen zu lassen. ComplianceOS extrahiert Textinhalte aus fuenf Formaten und ordnet sie den relevanten Standards und Domains zu.

<figure class="screenshot" markdown>
![Dokumente Uebersicht](../screenshots/dokumente/dokumente-overview.png)
<figcaption>Dokumente: Upload-Bereich oben, hochgeladene Dokumente mit Status und Metadaten unten</figcaption>
</figure>

---

## Unterstuetzte Formate

ComplianceOS verarbeitet fuenf gaengige Dokumentformate:

| Format | Erweiterung | Parser | Typische Inhalte |
|--------|-------------|--------|-----------------|
| **PDF** | `.pdf` | PyMuPDF | Richtlinien, Zertifikate, Audit-Reports, Compliance-Nachweise |
| **Word** | `.docx` | python-docx | Policies, Verfahrensanweisungen, Betriebshandbuecher |
| **Excel** | `.xlsx` | openpyxl | Massnahmenlisten, Asset-Register, Risikoanalysen |
| **Markdown** | `.md` | Direkt | Technische Dokumentation, Konfigurationsbeschreibungen |
| **Text** | `.txt` | Direkt | Konfigurationsdateien, Logs, Notizen |

!!! info "PDF-Upload"
    Fuer PDF-Verarbeitung muss das Feature-Flag `ENABLE_PDF_UPLOAD=true` gesetzt sein (Standard: aktiviert). Sie koennen dies unter **Einstellungen > Feature Flags** pruefen.

---

## Dokument hochladen

1. Navigieren Sie zu **Dokumente** in der Seitenleiste
2. Klicken Sie auf den **Upload-Bereich** oder ziehen Sie Dateien per Drag & Drop hinein
3. Waehlen Sie eine oder mehrere Dateien aus
4. Der Upload und die automatische Analyse starten sofort

### Parser-Pipeline

Nach dem Upload durchlaeuft jedes Dokument eine automatische Verarbeitungspipeline:

| Schritt | Beschreibung | Dauer |
|---------|-------------|-------|
| **1. Upload** | Datei wird auf dem Server gespeichert | Sofort |
| **2. Parsing** | Text wird aus dem Dokument extrahiert | 1-5 Sekunden |
| **3. Analyse** | Inhalte werden mit Controls abgeglichen | 2-10 Sekunden |
| **4. Zuordnung** | Relevante Standards und Domains werden identifiziert | 1-2 Sekunden |

Der Fortschritt wird durch den Analyse-Status angezeigt:

- **Pending**: Upload erfolgreich, Analyse laeuft
- **Analysiert**: Verarbeitung abgeschlossen
- **Fehler**: Problem bei der Verarbeitung (z.B. geschuetztes PDF)

---

## Dokumente-Uebersicht

Die Uebersicht listet alle hochgeladenen Dokumente mit:

| Spalte | Beschreibung |
|--------|-------------|
| **Dateiname** | Name der hochgeladenen Datei |
| **Format** | Erkannter Dateityp (PDF, DOCX, XLSX, MD, TXT) |
| **Groesse** | Dateigroesse |
| **Upload-Datum** | Zeitpunkt des Uploads |
| **Status** | Analyse-Status (Pending, Analysiert, Fehler) |

Klicken Sie auf ein Dokument um die Detailansicht zu oeffnen.

---

## Detailansicht

Die Detailansicht zeigt alle Informationen zu einem hochgeladenen Dokument:

<figure class="screenshot" markdown>
![Dokument Detail](../screenshots/dokumente/dokument-detail.png)
<figcaption>Dokument-Detail: Metadaten, Analyse-Status und extrahierter Textinhalt</figcaption>
</figure>

### Metadaten

| Feld | Beschreibung |
|------|-------------|
| **Dateiname** | Originaler Dateiname |
| **Format** | Erkannter Dateityp |
| **Groesse** | Dateigroesse in KB/MB |
| **Upload-Datum** | Zeitpunkt des Uploads |
| **Analyse-Status** | Aktueller Verarbeitungsstand |

### Extrahierter Text

Der vollstaendige extrahierte Textinhalt wird angezeigt. Bei PDF- und Word-Dokumenten wird die Formatierung so weit wie moeglich beibehalten.

---

## Dokument loeschen

1. Oeffnen Sie das Dokument in der Detailansicht
2. Klicken Sie auf **Loeschen**
3. Bestaetigen Sie die Aktion

!!! warning "Unwiderruflich"
    Geloeschte Dokumente koennen nicht wiederhergestellt werden. Die Datei wird sowohl aus der Datenbank als auch vom Dateisystem entfernt.

---

## Tipps zur Dokumentenverwaltung

!!! tip "Vor dem Audit hochladen"
    Laden Sie relevante Dokumente (Policies, Betriebshandbuecher, Konfigurationen) **vor** einem Audit hoch. So kann die Audit-Engine die Dokumente als zusaetzliche Evidenz heranziehen.

!!! tip "Aktualitaet"
    Halten Sie die hochgeladenen Dokumente aktuell. Veraltete Policies oder abgelaufene Zertifikate koennen zu falschen Audit-Ergebnissen fuehren.

!!! tip "Benennungskonvention"
    Verwenden Sie aussagekraeftige Dateinamen wie `passwort-richtlinie-v2.1.pdf` statt `dokument1.pdf`. Die Dateinamen werden in der Uebersicht und in Findings als Referenz angezeigt.
