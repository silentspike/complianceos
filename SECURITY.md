# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 1.0.x   | :white_check_mark: |

---

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub
issues.**

ComplianceOS uses **GitHub Security Advisories** as the single channel
for responsible disclosure. Advisories are private, authenticated, and
integrated with our triage workflow — we do not operate a separate
mailbox or PGP key.

[Open a private advisory](https://github.com/silentspike/complianceos/security/advisories/new)

A machine-readable contact record per RFC 9116 lives at
[`docs/.well-known/security.txt`](docs/.well-known/security.txt). It
points at the same advisory URL as above.

---

## What to Include

- Description of the vulnerability
- Affected component / version
- Steps to reproduce (proof-of-concept code is welcome)
- Potential impact assessment (CVSS v3.1 vector if available)
- Suggested fix or mitigation (if any)
- Whether you wish to be credited publicly or remain anonymous

---

## Response SLAs

| Stage | Target |
|-------|--------|
| **Acknowledgment** of receipt | 24 hours |
| **Initial triage + severity classification** | 72 hours |
| **Fix or mitigation (Critical / High)** | 30 days |
| **Fix or mitigation (Medium)** | 60 days |
| **Fix or mitigation (Low)** | 90 days |
| **Public disclosure (coordinated)** | typically 90 days after report |

We may request extensions on the disclosure timeline for complex issues
that require coordination with downstream vendors. Such requests will be
explained transparently and only when strictly necessary.

---

## Disclosure Policy

We follow a coordinated disclosure model:

1. Report the vulnerability privately via the advisory channel above
2. Allow us reasonable time to address the issue before public
   disclosure
3. Avoid exploiting the vulnerability beyond what is necessary to
   demonstrate impact
4. Do not access, modify, or delete data that is not your own

We commit to:

- Acknowledging receipt within the SLA above
- Keeping the reporter informed of progress at meaningful milestones
- Crediting reporters in the published advisory and changelog (unless
  anonymity is requested)
- Not pursuing legal action against good-faith security researchers who
  follow this policy

---

## Out of Scope

The following are typically out of scope for this disclosure programme
(but high-quality reports may still be acknowledged):

- Findings against third-party services we use (please report to those
  vendors directly)
- Issues requiring physical access to a deployed customer instance
- Issues requiring fully privileged access on the host operating system
- Denial-of-service via resource exhaustion at the host level
- Reports without a working proof-of-concept against a current release

---

## Security Design

ComplianceOS is designed as an **on-premise application**:

- All data is stored locally in SQLite
- No telemetry or data collection
- Optional AI features (Anthropic Claude, BYOK) are opt-in
- No outbound network calls except optional AI queries (when configured)
- Database access uses parameterised queries (SQL injection prevention)
- File uploads are validated, type-checked, and sandboxed

The internal threat model and hardening notes for licensed customers are
delivered as part of the evaluation package.
