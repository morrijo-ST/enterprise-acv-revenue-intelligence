# Enterprise ACV & Revenue Intelligence

A Snowflake-backed business intelligence reference for recurring revenue, bookings, expirations, contract exposure, geography, and executive finance analysis.

> **Working public demo:** The repo includes a deterministic synthetic customer/contract portfolio, executable ACV logic, an interactive Streamlit app, tests, and reproducible run instructions. See [`DEMO.md`](DEMO.md).

> **Portfolio note:** All public data, names, identifiers, and examples are synthetic or generalized. No employer datasets or proprietary implementation details are included.

## Try It

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Business Problem

Recurring-revenue businesses need a consistent way to understand current ACV, bookings, renewals, expirations, contract mix, geography, and forward exposure. This demo shows how those concepts can be normalized into a governed analytical model for FP&A and management reporting.

## Demo Capabilities

- starting and ending ACV
- net ACV movement and growth
- expiring ACV exposure
- bookings
- renewal / expansion / contraction / churn movement classes
- regional and product filtering
- customer-level drilldown

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

`Snowflake` `Power BI` `DAX` `SQL` `Python` `Streamlit` `Pandas` `Plotly` `Data Modeling` `FP&A`

## Repository Structure

```text
.
├── app.py
├── core.py
├── synthetic.py
├── requirements.txt
├── DEMO.md
├── docs/
│   ├── case-study.md
│   ├── architecture.md
│   ├── metric-definitions.md
│   ├── business-rules.md
│   ├── data-dictionary.md
│   ├── security.md
│   └── runbook.md
└── tests/
    └── test_core.py
```

## Demo Status

- [x] Public-safe project definition
- [x] Synthetic customer / ACV portfolio
- [x] Executable ACV analytics
- [x] Interactive dashboard demo
- [x] Automated tests
- [x] Documentation / controls
- [ ] Hosted live-demo URL
- [ ] Sanitized Power BI screenshot gallery
- [ ] Recorded walkthrough

## Architectural Focus

The public reference version emphasizes transparent finance definitions, deterministic data generation, reusable metrics, clean filtering, and separation between business logic and presentation.
