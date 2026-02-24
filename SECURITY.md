# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via [GitHub Security Advisories](https://github.com/silentspike/complianceos/security/advisories/new).

You can also reach us directly at: https://github.com/silentspike

### What to Include

- Description of the vulnerability
- Steps to reproduce
- Potential impact assessment
- Suggested fix (if any)

### Response Timeline

| Stage | Target |
|-------|--------|
| Acknowledgment | 24 hours |
| Triage & Assessment | 7 days |
| Fix (Critical/High) | 30 days |
| Fix (Medium/Low) | 90 days |

### Disclosure Policy

We follow a 90-day coordinated disclosure policy. We ask that you:

1. Report the vulnerability privately using the method above
2. Allow us reasonable time to address the issue before public disclosure
3. Avoid exploiting the vulnerability beyond what is necessary to demonstrate it

We will credit reporters in our changelog (unless anonymity is requested).

## Security Design

ComplianceOS is designed as an **on-premise application**:

- All data is stored locally in SQLite
- No telemetry or data collection
- Optional AI features (Claude) are opt-in via `[ai]` install extra
- No external network calls except optional AI queries
- All user input is parameterized (SQL injection prevention)
- File uploads are validated and sanitized
