# NIS2 (EU-Richtlinie 2022/2555)

> **Kontext:** Die NIS2-Richtlinie ersetzt die NIS1-Richtlinie und erweitert
> den Kreis der regulierten Einrichtungen. In Deutschland erfolgt die
> Umsetzung ueber das KRITIS-Dachgesetz und die Aktualisierung des
> BSI-Gesetzes.

---

## Geltungsbereich

NIS2 unterscheidet zwischen **wesentlichen Einrichtungen** (Annex I) und
**wichtigen Einrichtungen** (Annex II). Wesentliche Einrichtungen umfassen
unter anderem Energie, Verkehr, Bankwesen, Finanzmarkt-Infrastruktur,
Gesundheit, Trinkwasser, Abwasser, digitale Infrastruktur, IKT-
Dienstemanagement, oeffentliche Verwaltung und Weltraum. Wichtige
Einrichtungen umfassen unter anderem Post- und Kurierdienste,
Abfallwirtschaft, Chemikalien, Lebensmittelproduktion, verarbeitendes
Gewerbe und digitale Anbieter.

In Deutschland kommen Schwellwerte aus dem **KRITIS-Dachgesetz** zur
Anwendung — die Einstufung erfolgt branchenspezifisch ueber Versorgungs-
und Umsatz-Kennzahlen.

---

## Pflichten nach Article 21 (Risikomanagement-Massnahmen)

Article 21 NIS2 listet zehn Felder, fuer die alle regulierten Einrichtungen
Massnahmen umsetzen muessen:

1. Risikoanalyse- und Sicherheits-Konzepte fuer Informationssysteme
2. Bewaeltigung von Sicherheitsvorfaellen
3. Aufrechterhaltung des Betriebs (Backup-Management, Disaster Recovery,
   Krisenmanagement)
4. Sicherheit der Lieferkette
5. Sicherheit beim Erwerb, der Entwicklung und der Wartung von Netz- und
   Informationssystemen
6. Konzepte und Verfahren zur Bewertung der Wirksamkeit der Risikomanagement-
   Massnahmen
7. Grundlegende Verfahren der Cyberhygiene und Schulung im Bereich Cyber-
   sicherheit
8. Konzepte und Verfahren fuer den Einsatz von Kryptografie und Verschluesselung
9. Sicherheit des Personals, Konzepte fuer die Zugriffskontrolle und Asset-
   Management
10. Verwendung von Loesungen zur Multi-Faktor-Authentifizierung oder
    kontinuierlicher Authentifizierung sowie gesicherten Kommunikations- und
    Notfallkommunikationssystemen

---

## Meldepflichten (Article 23)

Sicherheitsvorfaelle sind in drei Stufen zu melden:

| Frist | Pflicht |
|---|---|
| **24 Stunden** | Frueh-Warnung an die zustaendige Behoerde (in Deutschland: BSI) — initiale Bewertung |
| **72 Stunden** | Vollstaendige Vorfalls-Meldung mit detaillierter Bewertung |
| **1 Monat** | Abschluss-Bericht mit Ursache und ergriffenen Massnahmen |

Bei wesentlichen Einrichtungen kommen Pflichten zur Information der
betroffenen Empfaenger und ggf. zur oeffentlichen Mitteilung hinzu.

---

## ComplianceOS-Mapping

| NIS2-Pflicht (Art. 21) | ComplianceOS-Domain | Anzahl Controls |
|---|---|---|
| Risikoanalyse + Konzepte | RISK + CONFIG | 12 |
| Bewaeltigung von Vorfaellen | INCIDENT | 8 |
| Aufrechterhaltung des Betriebs | BCP + BACKUP | 18 |
| Sicherheit der Lieferkette | SUPPLY | 6 |
| Sichere Entwicklung + Wartung | CONFIG + VULN | 14 |
| Bewertung der Wirksamkeit | LOGGING | 8 |
| Cyberhygiene + Schulung | ACCESS + AWARENESS | 10 |
| Kryptografie | CRYPTO | 11 |
| Personal + Zugriffskontrolle | ACCESS + PII | 16 |
| MFA + sichere Kommunikation | ACCESS + CRYPTO | 9 |

Reports und Drift-Detection sind so konfigurierbar, dass sie die NIS2-
Berichts-Struktur direkt abbilden.

---

## Zustaendige Behoerden

In Deutschland: **BSI** (Bundesamt fuer Sicherheit in der Informationstechnik)
ist die zustaendige Behoerde fuer NIS2-Meldungen. Branchenspezifische
Aufsichtsbehoerden (z.B. **BNetzA** fuer Energie, **BaFin** fuer Finanz-
sektor) bleiben fuer ihre jeweiligen Sektoren weiterhin zustaendig.

---

## Verweise

- EU-Richtlinie 2022/2555 (NIS2): [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- KRITIS-Dachgesetz (Bundesgesetzblatt — Inkraftsetzung 2024-2025)
- BSI Cybersicherheitsstrategie 2021

ComplianceOS-Doku zum [Standards-Ueberblick](../../referenz/standards.md).
