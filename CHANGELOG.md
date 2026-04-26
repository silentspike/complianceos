# Changelog

All notable changes to ComplianceOS will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2026-04-26

### Added
- 3 additional ROI scenarios in `docs/business/roi.md`: Krankenhaus
  (B3S + DSGVO + KHZG), Finanzdienstleister Mittelstand
  (BAIT/VAIT/ZAIT + DORA), Automotive-Zulieferer (TISAX Level 2/3) —
  now 6 illustrative scenarios total
- 6 regulation-specific detail pages under `docs/business/regulations/`:
  NIS2, B3S Krankenhaus, BAIT/VAIT/ZAIT, DORA, BSI IT-Grundschutz,
  TISAX. Linked from `for-who.md`, navigable via mkdocs sidebar
- `docs/architecture/control-matrix-workflow.md`: explicit description
  of the three-tier SSOT topology (toolkit canonical → public-binary
  embed → customer-override via `COMPLIANCEOS_CONTROL_MATRIX` env-var)
  with embed pattern, customer-override walkthrough, sync process,
  extending-base-set example
- `docs/.well-known/security.txt` per RFC 9116 (Contact, Expires,
  Preferred-Languages, Canonical, Policy)

### Changed
- Installation guide rewritten to reflect the EULA evaluation flow:
  no `git clone` / `docker compose up`, instead the issue-template
  request-and-private-delivery flow (matches the §3.2 sprint decision
  in v1.0.1)
- `SECURITY.md` consolidated to a single GitHub-Security-Advisory
  channel — no separate security mailbox, no PGP key, no public email
  surface anywhere in the repo. SLAs explicitly listed (24h ack /
  72h triage / 30d critical / 60d medium / 90d low)
- Evaluation request issue template no longer asks for an email
  address; communication happens inside the GitHub issue thread

### Fixed
- Three dangling links to the removed `schnellstart/docker.md` page
  (in `docs/index.md` sitemap and `docs/referenz/faq.md`) — found by
  `mkdocs build --strict`

### CI / Tooling
- `gitleaks` workflow switched from the licensed `gitleaks-action@v2`
  to a direct invocation of the upstream binary (no license required
  for org-owned repositories)

## [1.0.1] - 2026-04-26

### Added
- Architecture deep-dive page `docs/architecture.md` (pipeline,
  domains, standards)
- Target-audience and ROI documentation:
  `docs/business/for-who.md`, `docs/business/roi.md`
- Synthetic end-to-end sample audit report:
  `docs/samples/sample-audit-report.html`
- `evaluation_request.yml` issue template with EULA acknowledgement
- `gitleaks` + `dependabot` workflows; org-profile published

### Changed
- Public repo restructured for evaluation-focused enterprise
  discovery (proprietary EULA, no public binary downloads)
- `LICENSE` consolidated to proprietary across public marketing repo
  and source repo
- Embedded `assets/control-matrix.yaml` sanitised — homelab-specific
  IPs and M365 container references replaced with placeholders;
  toolkit-generic template shipped as default

### Removed
- `docker-compose.yml` and `docs/schnellstart/docker.md` — the
  evaluation flow no longer assumes self-service container start

## [1.0.0] - 2026-02-24

### Added
- 9 compliance standards: ISO 27001, ISO 22301, ISO 27005, ISO 27017, ISO 27018, ISO 27035, NIS2, BSI IT-Grundschutz, DSGVO
- 135 audit controls across 12 domains with 2,246 semantic AUDIT-CHECKs
- Chat-first interface with Claude AI integration for compliance guidance
- Automated audit engine with parallel check execution
- Intent classification system (9 intents) with built-in responses
- Document pipeline supporting PDF, DOCX, XLSX, Markdown, and plain text
- Policy generator with 6 templates (password, backup, incident, access, ISMS, data protection)
- Drift detection for regression analysis between audit runs
- Remediation tracking with assignment, deadlines, and verification workflow
- Cross-standard control mapping across all 9 standards
- Executive risk dashboard with business impact analysis and risk matrix
- Multi-project support with project-scoped data isolation
- Health check and Prometheus metrics endpoints
- Docker support with multi-stage builds and Compose
- Alembic database migrations
- Obsidian Prism design system (dark theme, jewel-tone colors)
- Keyboard shortcuts with command palette (Ctrl+K)
- Scheduled audit support (daily, weekly, monthly)
- Finding attachments and activity logging
