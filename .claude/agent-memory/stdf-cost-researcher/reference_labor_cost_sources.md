---
name: reference_labor_cost_sources
description: BLS/FRED sources for US manufacturing labor costs — historical series for incumbent cost modeling
type: reference
---

## US Manufacturing Labor Cost — Data Sources

### Wages only (T1)
- FRED series CES3000000008: "Average Hourly Earnings of Production and Nonsupervisory Employees, Manufacturing"
- URL: https://fred.stlouisfed.org/data/CES3000000008.txt (direct data download)
- Coverage: January 1939 to present (monthly)
- Key values (December): 2000=$14.50, 2005=$16.68, 2010=$18.79, 2015=$20.10, 2020=$23.16, 2023=$27.15, 2024=$28.34

### Total compensation (wages + benefits) (T1)
- BLS ECEC: "Employer Costs for Employee Compensation" — manufacturing sector
- URL: https://www.bls.gov/news.release/ecec.htm
- June 2025 values: wages=$30.94/hr, benefits=$15.36/hr, total=$46.30/hr
- Benefit burden rate = 15.36/30.94 = 49.6%
- Apply burden rate to historical wages to estimate total compensation (creates slight upward bias pre-2015)

### Annual work-year baseline
- Standard US manufacturing work year: 2,000 hours
- 2024 total loaded labor cost: ~$42.40/hr x 2,000 = ~$84,800/year per worker

### Key caveat
- The BLS ECEC benefit burden rate is not constant historically — benefits grew faster than wages pre-2015.
- Using the 2025 rate of 49.6% on pre-2015 wages creates ~5–10% upward bias in total comp estimates.
