# Glossar

Dieses Glossar erklärt die wichtigsten Begriffe die in ComplianceOS und der Compliance-Welt verwendet werden.

---

## A

**Annex A**
: Anhang A der ISO 27001 — enthält 93 Controls in 4 Kategorien (organisatorisch, personenbezogen, physisch, technologisch). ComplianceOS prüft diese Controls automatisch.

**Audit**
: Systematische, unabhängige Prüfung gegen definierte Anforderungen (Standards, Richtlinien, Controls). ComplianceOS unterscheidet Vollaudits (alle 135 Controls) und Domain-Audits (eine Domain).

**AUDIT-CHECK**
: Atomarer Prüfpunkt innerhalb eines Controls. Jeder Control besteht aus mehreren AUDIT-CHECKs die bei der Prüfung einzeln bewertet werden. ComplianceOS enthält 2.042 AUDIT-CHECKs.

## B

**BCP**
: Business Continuity Plan — Notfallplan der sicherstellt, dass kritische Geschäftsprozesse auch bei Störungen weiterlaufen. Wird durch ISO 22301 gefordert.

**BIA**
: Business Impact Analysis — Analyse der Auswirkungen von Ausfällen auf Geschäftsprozesse. Identifiziert kritische Systeme und definiert RPO/RTO-Ziele.

**BSI**
: Bundesamt für Sicherheit in der Informationstechnik — Deutsche Behörde die den IT-Grundschutz-Standard veröffentlicht.

**Burndown-Chart**
: Diagramm im Remediation-Modul das zeigt wie viele offene Findings über die Zeit abgebaut werden.

## C

**Claude AI**
: KI-Modell von Anthropic das ComplianceOS für Chat-Beratung, Audit-Bewertungen und Policy-Generierung nutzt. Optional — alle Kernfunktionen arbeiten auch ohne KI.

**Compliance**
: Einhaltung von Vorschriften, Standards und Richtlinien. ComplianceOS misst den Compliance-Grad als Prozentwert (0-100%).

**Confidence**
: Zuverlässigkeit einer automatischen Bewertung (0-100%). Werte unter 60% deuten darauf hin, dass eine manuelle Überprüfung sinnvoll ist.

**Control**
: Einzelne Sicherheitsanforderung aus einem Standard. ComplianceOS enthält 135 Controls verteilt auf 12 Domains. Jeder Control wird durch AUDIT-CHECKs geprüft.

**Cross-Standard-Mapping**
: Zuordnung von Controls zu mehreren Standards. Zeigt Überschneidungen zwischen Standards und ermöglicht effiziente Multi-Standard-Compliance.

## D

**Domain**
: Thematische Gruppierung von Controls. ComplianceOS verwendet 12 Domains: ACCESS, BACKUP, BCP, CONFIG, CRYPTO, INCIDENT, LOGGING, MALWARE, NETWORK, PII, SUPPLY, VULN.

**Drift**
: Veränderung des Compliance-Status zwischen zwei Audit-Läufen. Positive Drift = Verbesserung, negative Drift (Regression) = Verschlechterung.

**DSFA**
: Datenschutz-Folgenabschätzung — Risikoanalyse die bei hohem Risiko für personenbezogene Daten durchzuführen ist (DSGVO Art. 35).

**DSGVO**
: Datenschutz-Grundverordnung (EU 2016/679) — EU-weite Verordnung zum Schutz personenbezogener Daten. Seit Mai 2018 in Kraft.

## E

**EDR**
: Endpoint Detection and Response — Sicherheitslösung zur Erkennung und Reaktion auf Bedrohungen an Endgeräten.

**Evidence**
: Nachweis für die Einhaltung oder Abweichung eines Controls. Kann technischer Natur sein (Konfigurationsdateien, Logs) oder organisatorisch (Richtlinien, Schulungsnachweise).

## F

**Feature Flag**
: Konfigurationsschalter der einzelne Funktionen aktiviert oder deaktiviert (z.B. `teammates`, `policy_gen`, `pdf_upload`).

**Finding**
: Feststellung aus einem Audit — identifizierte Abweichung, Beobachtung oder Verbesserungsmöglichkeit. Jedes Finding hat eine Severity (Major NC, Minor NC, Observation, OFI).

## G

**Gap**
: Lücke zwischen Ist-Zustand und Soll-Zustand. Ein Finding beschreibt immer einen Gap.

## H

**Heatmap**
: Farbcodierte Matrix die die Verteilung von Findings nach Domain und Severity visualisiert. Dunkle Zellen = viele Findings.

## I

**ISMS**
: Information Security Management System — Managementsystem für Informationssicherheit nach ISO 27001. Umfasst Richtlinien, Prozesse, Verantwortlichkeiten und technische Massnahmen.

## K

**KI**
: Künstliche Intelligenz — in ComplianceOS optional eingesetzt für Chat-Beratung, Audit-Bewertungen und Policy-Generierung (via Claude AI).

## M

**Major NC**
: Schwerwiegende Nichtkonformität — eine fehlende oder nicht wirksame Sicherheitsmassnahme die ein direktes Risiko darstellt. Erfordert sofortige Massnahmen.

**MFA**
: Multi-Faktor-Authentifizierung — Authentifizierung mit mindestens zwei unabhängigen Faktoren (z.B. Passwort + Token).

**Minor NC**
: Geringfügige Nichtkonformität — eine vorhandene aber nicht vollständig konforme Sicherheitsmassnahme. Erfordert zeitnahe Behebung.

## N

**NC**
: Non-Conformity — Nichtkonformität oder Abweichung von einer Anforderung. Unterschieden in Major NC und Minor NC.

**NIS2**
: Network and Information Security Directive 2 (EU 2022/2555) — EU-Richtlinie die Anforderungen an die Cybersicherheit wesentlicher und wichtiger Einrichtungen definiert.

**ntfy**
: Einfacher Push-Benachrichtigungsdienst. ComplianceOS kann Benachrichtigungen (Audit abgeschlossen, neue Major NCs) über ntfy senden.

## O

**Observation**
: Beobachtung — ein Finding das auf Verbesserungspotenzial hinweist, aber keine direkte Nichtkonformität darstellt.

**OFI**
: Opportunity for Improvement — Verbesserungsmöglichkeit die über die Mindestanforderungen hinausgeht. Optional umzusetzen.

## P

**PII**
: Personally Identifiable Information — Personenbezogene Daten die eine natürliche Person identifizierbar machen.

**Policy**
: Richtlinie — dokumentierte Sicherheitsanforderung einer Organisation (z.B. Passwort-Richtlinie, Backup-Richtlinie).

## R

**RBAC**
: Role-Based Access Control — Rollenbasierte Zugriffskontrolle bei der Berechtigungen an Rollen statt an einzelne Benutzer vergeben werden.

**Reasoning Chain**
: Nachvollziehbare Begründungskette einer KI-Bewertung. Zeigt Schritt für Schritt warum ein Finding eine bestimmte Severity erhalten hat.

**Remediation**
: Massnahme zur Behebung einer Abweichung. ComplianceOS bietet Kanban-Board, Listen- und Kalender-Ansicht für das Remediation-Tracking.

**RPO**
: Recovery Point Objective — Maximaler akzeptabler Datenverlust-Zeitraum. Definiert wie alt das letzte Backup maximal sein darf.

**RTO**
: Recovery Time Objective — Maximale akzeptable Wiederherstellungszeit. Definiert wie lange ein System maximal ausfallen darf.

## S

**Scope**
: Geltungsbereich eines Audits — definiert welche Standards, Domains und Systeme geprüft werden.

**Severity**
: Schweregrad eines Findings. Vier Stufen: Major NC (schwerwiegend), Minor NC (geringfügig), Observation (Beobachtung), OFI (Verbesserungsmöglichkeit).

**SIEM**
: Security Information and Event Management — System zur zentralen Sammlung, Korrelation und Analyse von Sicherheitsereignissen.

**SoA**
: Statement of Applicability — Erklärung zur Anwendbarkeit der Controls aus ISO 27001 Annex A. Dokumentiert welche Controls anwendbar sind und welche nicht.

**SSE**
: Server-Sent Events — Technologie für Echtzeit-Updates vom Server zum Browser. ComplianceOS nutzt SSE für den Live-Fortschritt bei Audits.

## T

**TOM**
: Technische und Organisatorische Massnahmen — Schutzmassnahmen die sowohl technische (Verschlüsselung, Firewall) als auch organisatorische (Richtlinien, Schulungen) Aspekte umfassen.

## V

**Vollaudit**
: Audit-Modus der alle 135 Controls über alle 12 Domains prüft. Empfohlen für die Erstprüfung und regelmässige Compliance-Checks.
