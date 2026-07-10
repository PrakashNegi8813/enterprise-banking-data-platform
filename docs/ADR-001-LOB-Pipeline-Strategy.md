# ADR-001: Independent LOB Pipelines

## Status
Accepted

## Context

Consumer Banking, Mortgage, Credit Card, Wealth, and Commercial Banking have different source systems, SLAs, business rules, and deployment schedules.

A single monolithic pipeline would increase coupling and reduce resilience.

## Decision

Each LOB will maintain an independent end-to-end pipeline from Landing through Gold.

Shared enterprise datasets (for example, Enterprise Complaint Silver) will be consumed rather than recreated.

## Consequences

### Advantages

- Failure isolation
- Independent deployments
- Independent schedules
- Reusable enterprise data
- Easier maintenance

### Disadvantages

- More pipelines to manage
- Additional orchestration