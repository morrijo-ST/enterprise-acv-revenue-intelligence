# Business Rules — Enterprise ACV & Revenue Intelligence

**BR-001 — ACV definition**  
Annual contract value must be calculated from approved contract and finance fields using one governed definition.

**BR-002 — GACV movement**  
Growth ACV should distinguish expansion, contraction, renewal, and non-renewal movements so net changes remain explainable.

**BR-003 — Expiration timing**  
Contract expirations must be aligned to the governed fiscal calendar and renewal window.

**BR-004 — Geography mapping**  
Country and region assignments follow a documented mapping hierarchy; fallback logic must be explicit and testable.

**BR-005 — Customer hierarchy**  
Revenue and contract exposure must roll to one governed customer hierarchy for management reporting.

**BR-006 — FX consistency**  
Currency translation must use the designated reporting rate and period logic consistently across measures.

**BR-007 — Weighted contract metrics**  
Weighted averages must use the documented financial weighting basis rather than simple arithmetic averages where material.

**BR-008 — Missing keys**  
Rows with missing customer, contract, or geography keys must be surfaced for data-quality review rather than silently dropped.

**BR-009 — One date dimension**  
The public reference model uses one governed date table for all report period logic.

**BR-010 — Metric traceability**  
Every executive KPI should be traceable to its underlying fact fields and calculation logic.