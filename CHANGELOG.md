# Changelog

All notable changes to ComplianceOS will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
