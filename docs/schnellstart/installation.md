# Installation

ComplianceOS is proprietary software distributed under a [commercial EULA](../../LICENSE).
There are no public binary downloads, container images or `git clone`able source artifacts.
Installation happens as part of an evaluation engagement or commercial licensing
agreement — we deliver the artifact, you deploy it on your own infrastructure.

---

## How to obtain ComplianceOS

### 1. Request an evaluation

Open an [Evaluation Request issue](https://github.com/silentspike/complianceos/issues/new?template=evaluation_request.yml).
The form captures the information we need to scope a fitting evaluation:

- Organisation, role and use case
- Target standards (ISO 27001, ISO 22301, BSI, NIS2, …)
- Approximate deployment size (single host, VM, on-prem fleet)
- Acknowledgement of the EULA terms

We respond within two business days.

### 2. Receive the evaluation package

After scoping you receive privately:

- A signed container image (or a self-contained binary, depending on platform)
- An activation code tied to your deployment
- A short onboarding guide that maps to the screens documented under
  [Bedienung](../bedienung/dashboard.md)
- Optional: a guided remote walkthrough of the audit workflow

### 3. Deploy on your own infrastructure

ComplianceOS runs entirely on premise. The runtime requirements are modest:

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **CPU** | 2 cores | 4 cores |
| **RAM** | 1 GB | 2 GB |
| **Disk** | 1 GB | 5 GB (for audit data + reports) |
| **OS** | Linux x86_64 | Linux x86_64 |
| **Browser (clients)** | Chrome 90+ / Firefox 90+ / Safari 15+ / Edge 90+ | latest stable |

No outbound internet connectivity is required for the core audit engine —
findings, reports, policies and remediation tracking all run locally.

### 4. Optional: enable AI features (BYOK)

Some features (chat assistant, AI-assisted finding interpretation, policy
generation) require an Anthropic API key. ComplianceOS uses a Bring-Your-Own-Key
model: your key, your account, your audit trail. Without a key the platform
remains fully functional — the AI-assisted features simply stay disabled.

---

## What you can already see in this public repository

Even without a deployed instance, this repository documents the product in
detail:

- [Architecture overview](../architecture.md) — pipeline, domains, standards
- [Bedienung](../bedienung/dashboard.md) — full operating manual with
  **24 screenshots** across dashboard, audits, chat, findings, policies,
  reports and setup
- [Demo videos](../videos/audit-workflow.mp4) — short clips of audit
  workflow, finding lifecycle, policy generation, drift detection and chat
- [Sample audit report](../samples/sample-audit-report.html) — a synthetic
  end-to-end report rendered in the actual export format
- [Standards reference](../referenz/standards.md) — the nine compliance
  frameworks we cover

This is enough material for a procurement or security review committee to
assess fit before requesting an evaluation.

---

## Frequently asked

**Why no public download?**
ComplianceOS encodes proprietary control mappings, scoring logic and audit
heuristics. Distributing the binary publicly would expose the dependency
fingerprint of the build and undermine the value proposition for commercial
customers. The evaluation flow gives qualified evaluators full access on their
own infrastructure without that exposure.

**Can I see the source code?**
The audit toolkit definitions (control matrix, schemas) are openly documented
under [Architecture](../architecture.md). The runtime source code stays
private.

**How long does an evaluation last?**
Standard evaluation period is 30 days, extendable on request. Activation codes
are tier-bound and time-bound; expiry triggers a graceful read-only mode rather
than data loss.

**What happens to evaluation data afterwards?**
The data lives entirely on your infrastructure. We never receive a copy. If you
choose not to convert to a commercial license, simply stop the container — the
data directory is yours to archive or delete.
