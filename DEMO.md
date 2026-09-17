# Run the Public Demo

This repository includes a deterministic synthetic-data demo. No external credentials or proprietary datasets are required.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Run tests with:

```bash
pytest -q
```

The app generates a reproducible synthetic recurring-revenue portfolio and supports region/product filtering, ACV movement analysis, expirations, and customer-level drilldown.
