# Engineering Standards

## Repository

- One responsibility per module.
- No business logic inside notebooks.
- Reusable logic belongs in `src`.

## Python

- Follow PEP 8.
- Use type hints where appropriate.
- Use logging instead of print statements.
- Raise meaningful exceptions.

## Databricks

- Notebooks orchestrate workflows only.
- All reusable logic resides in Python modules.

## Git

- Never commit directly to `main`.
- Develop using feature branches.
- One feature branch per sprint.

## Azure

- Use Unity Catalog.
- No storage account keys.
- Prefer managed identity or service principals.

## Delta Lake

- Bronze: Raw ingestion.
- Silver: Cleansed and standardized.
- Gold: Business-ready analytics.

## Documentation

Every feature must include:
- Design notes
- Configuration updates (if applicable)
- README updates (when user-facing changes are introduced)