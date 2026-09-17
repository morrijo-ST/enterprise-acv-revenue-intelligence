# Operations Runbook — Enterprise ACV & Revenue Intelligence

## Refresh Checks
1. Confirm Snowflake connectivity.
2. Confirm source views refreshed successfully.
3. Validate row counts for ACV, bookings, and expirations.
4. Review unmapped customer / geography exceptions.
5. Refresh the semantic model.
6. Reconcile headline KPIs to warehouse control totals.

## Common Failures
### Missing source data
Pause publication, identify the failed source, and document whether the report is partial.

### Mapping exceptions
Route unknown customer, product, country, or region values to the mapping exception list.

### KPI mismatch
Compare DAX result to warehouse-side control totals and inspect filter context, relationship behavior, and period logic.

### Refresh failure
Retry after validating gateway / credential / capacity health; document the final refresh timestamp.

## Publication Control
Do not publish executive outputs until headline ACV, bookings, expirations, and period totals reconcile to the approved control source.
