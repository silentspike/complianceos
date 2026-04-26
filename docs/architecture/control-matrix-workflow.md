# Control-Matrix Workflow

> **Kontext:** Die Control-Matrix ist das Herzstueck von ComplianceOS — sie
> definiert WAS auditiert wird (135 Controls in 12 Domains, 2246 AUDIT-CHECKs)
> und liefert das Cross-Standard-Mapping zu allen unterstuetzten Standards.
> Diese Seite beschreibt, woher die Matrix kommt, wie sie ins Public-Binary
> gelangt und wie Kunden-Erweiterungen funktionieren.

---

## SSOT-Topologie

ComplianceOS pflegt die Matrix in drei Ebenen mit klarer Hierarchie:

```text
┌─────────────────────────────────────────────────────────────┐
│  1. Toolkit-Matrix (canonical SSOT)                         │
│     Pfad: audit-toolkit/control-matrix.yaml                 │
│     Inhalt: 135 generische Controls, 12 Domains, 9 Standards│
│     Pflege:  Maintainer-Repo (silentspike intern)           │
└──────────────────────┬──────────────────────────────────────┘
                       │ generiert + sanitized
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  2. Public-Binary Embed                                     │
│     Pfad in Source: assets/control-matrix.yaml              │
│     Embed-Mechanismus: Go embed.FS                          │
│     Pflege:  Re-Generation aus Toolkit pro Release          │
│     Header:  "Public Template — Generic"                    │
└──────────────────────┬──────────────────────────────────────┘
                       │ ausgeliefert mit Binary
                       ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Customer-Override (Runtime)                             │
│     Mechanismus: Env-Var COMPLIANCEOS_CONTROL_MATRIX        │
│     Effekt:  Wenn gesetzt + Datei lesbar -> Override aktiv  │
│              Sonst Fallback auf eingebettete Matrix         │
│     Pflege:  Beim Kunden, eigene Datei mit Custom-Controls  │
└─────────────────────────────────────────────────────────────┘
```

Wichtig: **Customer-Override ersetzt das Embed komplett** — er erweitert
es nicht. Customer-Matrizen muessen entweder das volle Basis-Set kopieren
und ergaenzen, oder ein reduziertes Subset definieren (siehe weiter unten).

---

## Warum drei Ebenen?

| Ebene | Zielgruppe | Aenderung-Frequenz |
|---|---|---|
| Toolkit | Maintainer / Audit-Wissens-Pflege | wenn neue Standards / Controls dazukommen |
| Public-Binary | alle Eval-/Lizenz-Kunden | pro Release-Tag (z.B. v1.0.x) |
| Customer-Override | einzelner Kunde | pro Audit-Zyklus oder OEM-Klauseln |

Diese Trennung hat zwei Effekte:

1. **Konsistenz** — der canonical Toolkit-Stand ist immer die referenzielle
   Wahrheit; das Public-Binary ist eine Snapshot-Kopie davon
2. **Flexibilitaet** — Kunden koennen branchen- oder OEM-spezifische
   Zusatzklauseln (z.B. TISAX-OEM-Add-ons, BAFin-Sonderpruefungen) lokal
   pflegen, ohne auf einen neuen Binary-Release warten zu muessen

---

## Embed-Pattern (Go)

Die eingebettete Default-Matrix wird zur Compile-Zeit ueber `go:embed`
in das Binary geladen. Konzeptueller Auszug:

```go
package engine

import (
    _ "embed"
)

//go:embed assets/control-matrix.yaml
var embeddedMatrix []byte

// MatrixOverrideEnv ist die Env-Var, die einen Pfad auf eine eigene
// Matrix-Datei aufnimmt und das Embed zur Laufzeit ueberschreibt.
const MatrixOverrideEnv = "COMPLIANCEOS_CONTROL_MATRIX"

func loadMatrixBytes() ([]byte, error) {
    if path := os.Getenv(MatrixOverrideEnv); path != "" {
        b, err := os.ReadFile(path)
        if err == nil {
            return b, nil
        }
        // explizit gesetzter Pfad existiert nicht -> Fehler, kein Silent-Fallback
        return nil, fmt.Errorf("override matrix %q: %w", path, err)
    }
    return embeddedMatrix, nil
}
```

Verhalten:

- Env-Var **nicht gesetzt**: eingebettete Default-Matrix wird genutzt
- Env-Var gesetzt + Datei lesbar: Override-Datei wird genutzt
- Env-Var gesetzt + Datei nicht lesbar: **Fehler**, kein Silent-Fallback
  (so kann der Kunde einen Konfigurations-Fehler nicht uebersehen)

Den realen Loader-Test gibt es als `TestLoadMatrixBytes_*`-Suite (siehe
Vendor-Releases).

---

## Customer-Override anlegen

### Schritt 1: Basis-Matrix exportieren

Im laufenden Binary kann die aktuell aktive Matrix als YAML
exportiert werden:

```bash
complianceos matrix export --out customer-matrix.yaml
```

Das gibt entweder die eingebettete Default-Matrix aus (wenn keine Env-Var
gesetzt ist) oder die aktuelle Override-Datei. Sie ist YAML, gut lesbar
und kommentiert.

### Schritt 2: Custom-Controls hinzufuegen

```yaml
matrix_version: "1.0.0"
matrix_date: "2026-04-26"
description: "Customer override for ACME Corp — TISAX + OEM-spezifisch"

categories:
  - id: ACCESS
    name: Zugriffskontrolle
    # ... bestehende ACCESS-Controls bleiben ...

  - id: CUSTOM
    name: Customer-spezifische Controls
    description: |
      Kunden-Erweiterungen, nicht Teil des Basis-Sets.
    controls:
      - id: CUSTOM-001
        title: OEM-spezifische Verschluesselung in Datei-Transfer
        description: |
          Lieferanten-Vertrag verlangt AES-256-GCM bei allen Datei-
          Uebertragungen mit Status "Prototyp".
        standard_refs:
          - standard: TISAX
            ref: VDA-ISA Modul Prototype Protection
          - standard: ISO 27001
            ref: A.10 Cryptography
        severity_if_missing: major_nc
        verification_method: hybrid
        expected_evidence:
          - Verschluesselungs-Konfiguration aus File-Transfer-Komponente
          - Vertrags-Auszug der OEM-Klausel
        checks:
          - type: file_grep
            pattern: 'cipher\\s*=\\s*aes-256-gcm'
        interview:
          - "Welche Schluessel-Rotations-Frequenz wird fuer den Datei-Transfer eingehalten?"
```

### Schritt 3: Override aktivieren

```bash
export COMPLIANCEOS_CONTROL_MATRIX=/etc/complianceos/customer-matrix.yaml
complianceos serve
```

Beim naechsten Audit-Lauf werden alle Custom-Controls genauso behandelt
wie die Basis-Controls: sie erscheinen in Findings, Reports, Drift-
Detection, Cross-Standard-Mapping (sofern `standard_refs` gesetzt).

### Schritt 4: Validierung

```bash
complianceos matrix validate --file customer-matrix.yaml
```

Validiert das Schema (`schemas/control.schema.json`), prueft Domain-IDs,
Standard-References, eindeutige Control-IDs.

---

## Sync-Prozess Toolkit -> Binary -> Customer

```text
1. Toolkit-Matrix wird gepflegt (z.B. neuer NIS2-Anhang)
   audit-toolkit/control-matrix.yaml: matrix_version 1.0.0 -> 1.1.0

2. Sanitize + Re-Embed
   make embed-matrix
   -> assets/control-matrix.yaml mit Header "Public Template — Generic"

3. Release
   git tag v1.1.0 ; git push --tags
   -> Public-Binary mit neuer Default-Matrix verfuegbar

4. Customer-Update (optional)
   Neue Version installieren
   Wenn Customer-Override im Einsatz: Diff zu altem Embed pruefen,
   eigene Custom-Controls auf das neue Basis-Set merge'n
   complianceos matrix validate --file customer-matrix.yaml
```

Beim Versions-Sprung des Basis-Sets (z.B. ACCESS-007 wird neu hinzugefuegt)
muss der Kunde aktiv entscheiden, ob er das neue Control in sein Override-
Set uebernimmt — automatisch geschieht das nicht, weil der Override das
Embed komplett ersetzt.

Die Tracking-Issue
[#5](https://github.com/silentspike/complianceos/issues/5) im Public-Repo
bleibt das Sammelbecken fuer Aenderungen an diesem Workflow.

---

## Beispiel: Extending base set

Ein typisches Customer-Setup will das volle Basis-Set behalten und nur
zusaetzliche Controls hinzufuegen. Der einfachste Weg:

```bash
# 1. Aktuelles Basis-Set exportieren (oder aus dem assets/-Pfad kopieren)
complianceos matrix export --out customer-matrix.yaml

# 2. Eigene CUSTOM-Domain ans Ende anhaengen
cat custom-acme-controls.yaml >> customer-matrix.yaml

# 3. Validieren + aktivieren
complianceos matrix validate --file customer-matrix.yaml
export COMPLIANCEOS_CONTROL_MATRIX=$PWD/customer-matrix.yaml
complianceos serve
```

So bleibt das Basis-Set vollstaendig erhalten und alle Custom-Controls
liegen in einer separaten Domain (z.B. `CUSTOM`, `OEM_BMW`, `TISAX_OEM`).
Bei Binary-Updates kopiert der Kunde nur seine eigene Domain-Sektion in
das neue Export.

---

## Verweise

- [Architektur-Hauptseite](../architecture.md)
- [Standards-Referenz](../referenz/standards.md)
- Schema fuer Custom-Controls: `schemas/control.schema.json` (Bestandteil
  der Eval-Lieferung)
- Tracking-Issue [#5 — Document control-matrix SSOT workflow](https://github.com/silentspike/complianceos/issues/5)
