# Architecture — Enterprise ACV & Revenue Intelligence

## Reference Model

```text
CRM / Contracts / Finance / FX / Reference Data
                    |
                    v
                Snowflake
                    |
          Curated Fact Tables
     +--------------+--------------+
     |              |              |
    ACV          Bookings       Expirations
     |              |              |
     +-------+------+--------------+
             |
      Conformed Dimensions
 Customer / Contract / Product / Geography / Date
             |
             v
      Power BI Semantic Model
             |
             v
      Executive / FP&A Views
```

## Modeling Principles
- Separate facts from descriptive dimensions.
- Use a single governed date dimension.
- Push repeatable row-level transformations upstream where practical.
- Keep KPI logic centralized and documented.
- Preserve traceability from dashboard metric to source field.

## Major Subject Areas
### ACV
Recurring-revenue balances and movement by customer, product, geography, and contract.

### Bookings
New and renewal bookings with contract and customer context.

### Expirations
Forward-looking contract exposure and renewal timing.

### Geography
Country, region, and forecasting-region views with consistent mapping rules.

### Contract Analytics
Term, weighted averages, and customer-level exposure.

## Public Reference Design
The sanitized implementation will use a smaller star schema than the original enterprise model while preserving the architectural concepts that matter to buyers.