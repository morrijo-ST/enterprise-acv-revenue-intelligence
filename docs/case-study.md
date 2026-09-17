# Case Study — Enterprise ACV & Revenue Intelligence

## Business Problem
Recurring-revenue finance teams need a consistent view of ACV, GACV, bookings, expirations, contract exposure, customer concentration, geography, and forward-looking revenue risk. These metrics are often fragmented across CRM, contract, spreadsheet, and finance systems.

## Objective
Design a governed BI platform that standardizes recurring-revenue definitions and gives FP&A and management one analytical model for current balances, growth, expirations, contract behavior, and geographic performance.

## Solution Pattern
1. Consolidate commercial and finance sources in Snowflake.
2. Model core facts such as ACV, bookings, GACV, and expirations.
3. Create reusable dimensions for customer, contract, product, geography, and time.
4. Build a Power BI semantic layer with governed DAX measures.
5. Deliver executive and FP&A views for recurring-revenue analysis.

## Key Capabilities
- ACV balance analysis
- GACV growth analysis
- bookings and expirations
- contract-term analytics
- country / region analysis
- forecasting-region logic
- customer and product segmentation
- FX-aware reporting

## Public Portfolio Scope
The public reference version uses synthetic customers, contracts, regions, products, and revenue values. The architecture demonstrates the design pattern without exposing internal system names or proprietary logic.

## Future Enhancements
- cohort analysis
- contract renewal risk scoring
- scenario modeling
- warehouse-side metric materialization
- semantic-model CI/CD
