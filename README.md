# Enterprise ACV & Revenue Intelligence

A Snowflake-backed business intelligence platform for recurring revenue, bookings, expirations, contract exposure, geography, forecasting, and executive finance analysis.

> **Portfolio note:** This repository is a sanitized public reference derived from enterprise BI patterns. All data, names, identifiers, and examples used publicly are synthetic or generalized.

## Business Problem

Recurring-revenue businesses need a consistent way to understand current ACV, bookings, renewals, expirations, contract mix, geography, and forward exposure. Those metrics often live across CRM, contract, finance, spreadsheet, and data-warehouse sources.

This project demonstrates how to design an enterprise semantic model that turns those sources into a governed analytical platform for FP&A and management reporting.

## Core Capabilities

- ACV / recurring revenue balances
- GACV growth analysis
- bookings and expirations
- contract-term analytics
- geographic and country views
- forecasting-region logic
- customer and product hierarchies
- weighted contract metrics
- FX-aware analysis
- executive Power BI reporting

## Reference Architecture

```text
CRM / Contracts / Finance / Reference Data
                  |
                  v
              Snowflake
                  |
        Curated facts + dimensions
                  |
          Power BI semantic model
                  |
     DAX / governed business metrics
                  |
       Executive + FP&A dashboards
```

## Technology

`Snowflake` `Power BI` `DAX` `SQL` `Excel` `SharePoint` `Data Modeling` `FP&A`

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── case-study.md
│   ├── architecture.md
│   ├── metric-definitions.md
│   ├── business-rules.md
│   ├── data-dictionary.md
│   ├── security.md
│   └── runbook.md
├── sample-data/
├── sql/
├── dax/
├── diagrams/
├── screenshots/
└── tests/
```

## Portfolio Roadmap

- [x] Public-safe project definition
- [ ] Synthetic customer / contract / ACV dataset
- [ ] Simplified star-schema reference model
- [ ] DAX metric library
- [ ] Architecture diagram
- [ ] Sanitized dashboard screenshots
- [ ] Demo walkthrough

## Architectural Focus

The public reference version will emphasize a clean star schema, one governed date dimension, reusable measures, warehouse-side transformations where appropriate, and transparent finance definitions.