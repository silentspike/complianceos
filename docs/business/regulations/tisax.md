# TISAX (Trusted Information Security Assessment Exchange)

> **Kontext:** TISAX ist die Audit-Norm der deutschen Automobilindustrie,
> gepflegt durch die ENX Association. Sie basiert auf dem VDA ISA
> (Information Security Assessment), einem Fragenkatalog zur Selbst-
> beurteilung der Informationssicherheit. Pruefergebnisse sind ueber die
> ENX-Plattform zwischen Mitgliedern austauschbar — das spart
> Mehrfach-Audits derselben Lieferanten durch unterschiedliche OEMs.

---

## Pruefniveaus

TISAX kennt drei Pruefniveaus, die sich nach Schutzbedarf und Audit-
Tiefe unterscheiden:

| Level | Audit-Tiefe | Typische Anwendung |
|---|---|---|
| **Level 1** | Self-Assessment ohne Pruefer-Beteiligung | interne Erstbewertung, niedriger Schutzbedarf |
| **Level 2** | Self-Assessment + Plausibilitaets-Pruefung durch Pruefstelle (i.d.R. remote-basiert) | Standard-Lieferanten ohne hohen Verfuegbarkeits-/Geheimhaltungsbedarf |
| **Level 3** | vollstaendiger Vor-Ort-Audit mit detaillierter Beweiserhebung | Lieferanten mit Zugang zu hochschutzbeduerftigen Informationen, Prototypen, Personenbezogene-Daten in grossem Umfang |

Hoehere Level beinhalten alle Anforderungen der niedrigeren Level.

---

## VDA ISA Module

Der zugrundeliegende VDA-ISA-Fragenkatalog ist modular aufgebaut. Welche
Module zu erfuellen sind, haengt vom Schutzbedarf der bezogenen
Informationen ab:

| Modul | Inhalt | Verbindlich bei |
|---|---|---|
| **Information Security** | Basis-Informationssicherheit (ISO-27001-aehnlich) | jedem TISAX-Verfahren |
| **Prototype Protection** | Schutz von Vorserien-Fahrzeugen, Bauteilen | OEMs + Tier-1 mit Prototypen-Zugang |
| **Data Protection** | DSGVO Art. 28 Auftragsverarbeitung | bei Verarbeitung personenbezogener Daten |
| **Connected Vehicle** (Pilot/Erweiterung) | Vernetzte Fahrzeug-Backend-Anbindung | bei Connected-Car-Lieferanten |

Das Information-Security-Modul ist die Pflicht-Basis fuer **jedes**
TISAX-Verfahren. Module wie Prototype-Protection oder Data-Protection
werden je nach Lieferbeziehung hinzugewaehlt.

---

## Reife-Beurteilung

Anforderungen werden in einer Reife-Skala 0–5 bewertet:

| Reife | Bedeutung |
|---|---|
| 0 | nicht umgesetzt / nicht angemessen |
| 1 | teilweise und ad-hoc umgesetzt |
| 2 | ueberwiegend umgesetzt, dokumentiert |
| 3 | vollstaendig umgesetzt + dokumentiert + ueberprueft |
| 4 | proaktiv, kontinuierlich verbessert |
| 5 | innovativ, branchenfuehrend |

Die Soll-Reife ergibt sich pro Anforderung aus dem gewaehlten Pruefniveau.
Reife 3 ist typischerweise das Mindestmass fuer Level 2 und Level 3.

---

## Pruefablauf Level 3 (vereinfacht)

```text
1. Scoping              — welche Standorte, Module, Schutzbedarf
2. Self-Assessment      — Bewertung in der ENX-Plattform
3. Pruefer-Auswahl      — ENX-akkreditierte Pruefstelle
4. Pruef-Plan           — Vor-Ort-Termin-Vereinbarung
5. Vor-Ort-Audit        — Beweiserhebung + Interviews
6. Findings-Bearbeitung — Pruefer dokumentiert Reife-Bewertung
7. Bericht + Label      — bei Erfolg: TISAX-Label fuer 3 Jahre
8. ENX-Veroeffentlichung — Mitgliedern ueber Plattform zugaenglich
```

Bei groesseren Findings ist eine Nachpruefung erforderlich.

---

## OEM-spezifische Zusatzklauseln

Einige OEMs ergaenzen das VDA-ISA-Basis-Set durch eigene Anforderungen
(z.B. spezifische Verschluesselungs-Anforderungen, lokale Datenstandorte,
besondere Reaktionszeiten bei Vorfaellen). Diese werden vertraglich
zwischen OEM und Lieferant vereinbart und sind kein Teil des
TISAX-Pruefumfangs — Lieferanten muessen sie aber zusaetzlich erfuellen.

ComplianceOS unterstuetzt das ueber das Customer-Override-Pattern: Das
TISAX-Basis-Set wird als generischer Standard geladen, OEM-spezifische
Zusatz-Controls werden als Custom-Controls ergaenzt (siehe
[Architektur-Doku](../../architecture.md)).

---

## ComplianceOS-Mapping

| TISAX-Aspekt | ComplianceOS-Funktion |
|---|---|
| VDA-ISA Information Security | Standard-Plugin TISAX (mit Cross-Mapping zu ISO 27001) |
| VDA-ISA Prototype Protection | Domain CONFIG + ACCESS mit Tagging "prototype" |
| VDA-ISA Data Protection | Domain PII (DSGVO-Mapping) |
| Reife-Beurteilung | Findings-Workflow mit Reife-0-bis-5 als Severity-Mapping |
| OEM-Zusatzklauseln | Customer-Override (env-var COMPLIANCEOS_CONTROL_MATRIX) |
| Drift zwischen Audits | Automatischer Drift-Report seit letztem Self-Assessment |

---

## Verweise

- ENX Association: [enx.com/tisax](https://enx.com/en-us/tisax/)
- VDA ISA Fragenkatalog (aktuelle Version): VDA QMC
- ISO/IEC 27001:2022 (mappingrelevant)

ComplianceOS-Doku zum [Standards-Ueberblick](../../referenz/standards.md).
