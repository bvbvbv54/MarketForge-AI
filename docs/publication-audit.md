# Public Publication Audit

## Repository Audited

Original private repository: `C:\Users\moham\OneDrive\Documents\Hichem-AI`

Primary product code observed under: `C:\Users\moham\OneDrive\Documents\Hichem-AI\image-factory`

## Current Structure Observed

- `api/`: production API routes, auth, admin, exports, products, research, and integration endpoints.
- `dashboard/`: Next.js dashboard source.
- `database/`: models and database session setup.
- `services/`: acquisition, scraping, provider clients, AI generation, storage, verification, product intelligence, and accounting services.
- `tasks/`, `workers/`: background job pipeline.
- `docker/`, `docker-compose*.yml`: local and production-oriented container configuration.
- `outputs/`, `test-outputs/`, `test_images/`, `tmp/`: generated and test artifacts.
- `.env`, local databases, test spreadsheets, JSON reports, and setup guides.

## Safe To Expose

- New public name: MarketForge AI.
- Product value proposition.
- High-level workflow diagrams.
- Feature list.
- Roadmap.
- Sanitized screenshot plan.
- Technology stack names.
- Non-sensitive public-facing metrics and product outcomes.

## Must Remain Private

- `.env` and any local environment files.
- Database files such as `imagefactory.db` and `test.db`.
- API keys, provider credentials, service account secrets, and cloud storage keys.
- `api/`, `dashboard/`, `database/`, `services/`, `tasks/`, `workers/`, and production `docker` code.
- Scraping strategies, site-specific extractors, CAPTCHA handling, provider clients, and quota logic.
- AI prompts, image-generation pipelines, scoring algorithms, and automation workflows.
- Test fixtures containing real supplier/product examples.
- Generated outputs, reports, spreadsheets, and local admin reports.
- Existing implementation docs that describe internals in deployable detail.

## Public Strategy

Publish this sanitized MarketForge AI portfolio repository instead of the full Hichem-AI / Image Factory source repository. Keep the private repository for development and use this showcase for Upwork, LinkedIn, client demos, technical interviews, and startup presentations.
