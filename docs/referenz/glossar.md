# Glossar

Dieses Glossar erklaert die wichtigsten Begriffe die in ComplianceOS und der Compliance-Welt verwendet werden.

---

## A

**Annex A**
: Anhang A der ISO 27001 — enthaelt 93 Controls in 4 Kategorien (organisatorisch, personenbezogen, physisch, technologisch). ComplianceOS prueft diese Controls automatisch.

**Audit**
: Systematische, unabhaengige Pruefung gegen definierte Anforderungen (Standards, Richtlinien, Controls). ComplianceOS unterscheidet Vollaudits (alle 135 Controls) und Domain-Audits (eine Domain).

**AUDIT-CHECK**
: Atomarer Pruefpunkt innerhalb eines Controls. Jeder Control besteht aus mehreren AUDIT-CHECKs die bei der Pruefung einzeln bewertet werden. ComplianceOS enthaelt 2.042 AUDIT-CHECKs.

## B

**BCP**
: Business Continuity Plan — Notfallplan der sicherstellt, dass kritische Geschaeftsprozesse auch bei Stoerungen weiterlaufen. Wird durch ISO 22301 gefordert.

**BIA**
: Business Impact Analysis — Analyse der Auswirkungen von Ausfaellen auf Geschaeftsprozesse. Identifiziert kritische Systeme und definiert RPO/RTO-Ziele.

**BSI**
: Bundesamt fuer Sicherheit in der Informationstechnik — Deutsche Behoerde die den IT-Grundschutz-Standard veroeffentlicht.

**Burndown-Chart**
: Diagramm im Remediation-Modul das zeigt wie viele offene Findings ueber die Zeit abgebaut werden.

## C

**Claude AI**
: KI-Modell von Anthropic das ComplianceOS fuer Chat-Beratung, Audit-Bewertungen und Policy-Generierung nutzt. Optional — alle Kernfunktionen arbeiten auch ohne KI.

**Compliance**
: Einhaltung von Vorschriften, Standards und Richtlinien. ComplianceOS misst den Compliance-Grad als Prozentwert (0-100%).

**Confidence**
: Zuverlaessigkeit einer automatischen Bewertung (0-100%). Werte unter 60% deuten darauf hin, dass eine manuelle Ueberpruefung sinnvoll ist.

**Control**
: Einzelne Sicherheitsanforderung aus einem Standard. ComplianceOS enthaelt 135 Controls verteilt auf 12 Domains. Jeder Control wird durch AUDIT-CHECKs geprueft.

**Cross-Standard-Mapping**
: Zuordnung von Controls zu mehreren Standards. Zeigt Ueberschneidungen zwischen Standards und ermoeglicht effiziente Multi-Standard-Compliance.

## D

**Domain**
: Thematische Gruppierung von Controls. ComplianceOS verwendet 12 Domains: ACCESS, BACKUP, BCP, CONFIG, CRYPTO, INCIDENT, LOGGING, MALWARE, NETWORK, PII, SUPPLY, VULN.

**Drift**
: Veraenderung des Compliance-Status zwischen zwei Audit-Laeufen. Positive Drift = Verbesserung, negative Drift (Regression) = Verschlechterung.

**DSFA**
: Datenschutz-Folgenabschaetzung — Risikoanalyse die bei hohem Risiko fuer personenbezogene Daten durchzufuehren ist (DSGVO Art. 35).

**DSGVO**
: Datenschutz-Grundverordnung (EU 2016/679) — EU-weite Verordnung zum Schutz personenbezogener Daten. Seit Mai 2018 in Kraft.

## E

**EDR**
: Endpoint Detection and Response — Sicherheitsloesung zur Erkennung und Reaktion auf Bedrohungen an Endgeraeten.

**Evidence**
: Nachweis fuer die Einhaltung oder Abweichung eines Controls. Kann technischer Natur sein (Konfigurationsdateien, Logs) oder organisatorisch (Richtlinien, Schulungsnachweise).

## F

**Feature Flag**
: Konfigurationsschalter der einzelne Funktionen aktiviert oder deaktiviert (z.B. `teammates`, `policy_gen`, `pdf_upload`).

**Finding**
: Feststellung aus einem Audit — identifizierte Abweichung, Beobachtung oder Verbesserungsmoeglichkeit. Jedes Finding hat eine Severity (Major NC, Minor NC, Observation, OFI).

## G

**Gap**
: Luecke zwischen Ist-Zustand und Soll-Zustand. Ein Finding beschreibt immer einen Gap.

## H

**Heatmap**
: Farbcodierte Matrix die die Verteilung von Findings nach Domain und Severity visualisiert. Dunkle Zellen = viele Findings.

## I

**ISMS**
: Information Security Management System — Managementsystem fuer Informationssicherheit nach ISO 27001. Umfasst Richtlinien, Prozesse, Verantwortlichkeiten und technische Massnahmen.

## K

**KI**
: Kuenstliche Intelligenz — in ComplianceOS optional eingesetzt fuer Chat-Beratung, Audit-Bewertungen und Policy-Generierung (via Claude AI).

## M

**Major NC**
: Schwerwiegende Nichtkonformitaet — eine fehlende oder nicht wirksame Sicherheitsmassnahme die ein direktes Risiko darstellt. Erfordert sofortige Massnahmen.

**MFA**
: Multi-Faktor-Authentifizierung — Authentifizierung mit mindestens zwei unabhaengigen Faktoren (z.B. Passwort + Token).

**Minor NC**
: Geringfuegige Nichtkonformitaet — eine vorhandene aber nicht vollstaendig konforme Sicherheitsmassnahme. Erfordert zeitnahe Behebung.

## N

**NC**
: Non-Conformity — Nichtkonformitaet oder Abweichung von einer Anforderung. Unterschieden in Major NC und Minor NC.

**NIS2**
: Network and Information Security Directive 2 (EU 2022/2555) — EU-Richtlinie die Anforderungen an die Cybersicherheit wesentlicher und wichtiger Einrichtungen definiert.

**ntfy**
: Einfacher Push-Benachrichtigungsdienst. ComplianceOS kann Benachrichtigungen (Audit abgeschlossen, neue Major NCs) ueber ntfy senden.

## O

**Observation**
: Beobachtung — ein Finding das auf Verbesserungspotenzial hinweist, aber keine direkte Nichtkonformitaet darstellt.

**OFI**
: Opportunity for Improvement — Verbesserungsmoeglichkeit die ueber die Mindestanforderungen hinausgeht. Optional umzusetzen.

## P

**PII**
: Personally Identifiable Information — Personenbezogene Daten die eine natuerliche Person identifizierbar machen.

**Policy**
: Richtlinie — dokumentierte Sicherheitsanforderung einer Organisation (z.B. Passwort-Richtlinie, Backup-Richtlinie).

## R

**RBAC**
: Role-Based Access Control — Rollenbasierte Zugriffskontrolle bei der Berechtigungen an Rollen statt an einzelne Benutzer vergeben werden.

**Reasoning Chain**
: Nachvollziehbare Begruendungskette einer KI-Bewertung. Zeigt Schritt fuer Schritt warum ein Finding eine bestimmte Severity erhalten hat.

**Remediation**
: Massnahme zur Behebung einer Abweichung. ComplianceOS bietet Kanban-Board, Listen- und Kalender-Ansicht fuer das Remediation-Tracking.

**RPO**
: Recovery Point Objective — Maximaler akzeptabler Datenverlust-Zeitraum. Definiert wie alt das letzte Backup maximal sein darf.

**RTO**
: Recovery Time Objective — Maximale akzeptable Wiederherstellungszeit. Definiert wie lange ein System maximal ausfallen darf.

## S

**Scope**
: Geltungsbereich eines Audits — definiert welche Standards, Domains und Systeme geprueft werden.

**Severity**
: Schweregrad eines Findings. Vier Stufen: Major NC (schwerwiegend), Minor NC (geringfuegig), Observation (Beobachtung), OFI (Verbesserungsmoeglichkeit).

**SIEM**
: Security Information and Event Management — System zur zentralen Sammlung, Korrelation und Analyse von Sicherheitsereignissen.

**SoA**
: Statement of Applicability — Erklaerung zur Anwendbarkeit der Controls aus ISO 27001 Annex A. Dokumentiert welche Controls anwendbar sind und welche nicht.

**SSE**
: Server-Sent Events — Technologie fuer Echtzeit-Updates vom Server zum Browser. ComplianceOS nutzt SSE fuer den Live-Fortschritt bei Audits.

## T

**TOM**
: Technische und Organisatorische Massnahmen — Schutzmassnahmen die sowohl technische (Verschluesselung, Firewall) als auch organisatorische (Richtlinien, Schulungen) Aspekte umfassen.

## V

**Vollaudit**
: Audit-Modus der alle 135 Controls ueber alle 12 Domains prueft. Empfohlen fuer die Erstpruefung und regelmaessige Compliance-Checks.
