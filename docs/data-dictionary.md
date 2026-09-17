# Data Dictionary — Enterprise ACV & Revenue Intelligence

| Table | Field | Type | Description |
|---|---|---|---|
| dim_customer | customer_id | string | Synthetic customer key |
| dim_customer | customer_name | string | Fictional customer name |
| dim_customer | region | string | Reporting region |
| dim_contract | contract_id | string | Contract key |
| dim_contract | customer_id | string | Customer foreign key |
| dim_contract | start_date | date | Contract start |
| dim_contract | end_date | date | Contract end |
| fact_acv | contract_id | string | Contract foreign key |
| fact_acv | period | date | Reporting period |
| fact_acv | acv | decimal | Annual contract value |
| fact_bookings | booking_id | string | Booking transaction key |
| fact_bookings | contract_id | string | Contract foreign key |
| fact_bookings | booking_date | date | Booking date |
| fact_bookings | booking_value | decimal | Booking value |
| fact_expirations | contract_id | string | Contract foreign key |
| fact_expirations | expiration_date | date | Contract expiration |
| fact_expirations | expiring_acv | decimal | ACV scheduled to expire |
| dim_product | product_id | string | Product / suite key |
| dim_geo | country_code | string | Country key |
| dim_geo | region | string | Reporting region |

All public examples are synthetic.