# Architecture

MarketForge AI is presented publicly as an AI commerce intelligence platform. This document describes the system at product architecture level without exposing proprietary internals.

## System Context

```mermaid
flowchart TB
    User["Seller / Operator"] --> UI["Web Dashboard"]
    UI --> API["API Layer"]
    API --> Research["Product Research Service"]
    API --> Assets["Asset Management Service"]
    API --> Jobs["Job Orchestration"]
    Research --> Providers["Research Provider Interfaces"]
    Providers --> Keywords["Keyword Intelligence"]
    Providers --> Competitors["Competitor Signals"]
    Research --> Scoring["Opportunity Scoring"]
    Scoring --> Recommendations["Seller Recommendations"]
    Recommendations --> Listing["Listing Automation"]
    Recommendations --> Visuals["Image Strategy"]
    Visuals --> ImageAI["AI Image Generation"]
    Assets --> Storage["Cloud Storage"]
    Listing --> Export["Marketplace Export"]
    Storage --> Export
    Research --> PDF["Report Generation"]
```

## Core Product Workflow

```mermaid
sequenceDiagram
    participant Seller
    participant Dashboard
    participant Research
    participant Intelligence
    participant ImageFactory
    participant Export

    Seller->>Dashboard: Submit product idea, URL, ASIN, or CSV
    Dashboard->>Research: Start product research
    Research->>Intelligence: Analyze keywords, demand, and competitors
    Intelligence-->>Research: Opportunity score and explanation
    Research->>ImageFactory: Create AI image plan
    Research->>Export: Prepare listing and report package
    Export-->>Seller: PDF, CSV, metadata, and asset package
```

## Public Boundary

Included in this showcase:

- Product positioning.
- Feature descriptions.
- Architecture diagrams.
- Roadmap.
- Screenshot plan.

Excluded from this showcase:

- Production source code.
- Scraping strategies and site-specific extractors.
- AI prompts, scoring internals, and provider logic.
- API keys, tokens, cloud credentials, and private URLs.
- Database files and internal schemas.
- Customer, supplier, or product research data.
