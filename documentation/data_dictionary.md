# Data Dictionary

**Project Title:** Global AI Adoption in Education: A Comprehensive Global Analysis  
**Dataset Source:** `data/raw/Global AI in Education.csv`  
**Processed Target:** `data/processed/cleaned_ai_education.csv`  
**Total Records:** 1,360 rows  
**Date Range:** January 2015 to April 2026 (136 observation months per country across 10 countries)  

---

## 1. Raw Dataset Schema

| Column Name | Description | Data Type | Example | Min Value | Max Value | Notes / Handling |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `year` | Calendar year of observation | Integer (`int64`) | `2015` | `2015` | `2026` | Discrete time dimension spanning 12 distinct years. |
| `month` | Calendar month of observation (1–12) | Integer (`int64`) | `1` | `1` | `12` | 2015–2025 contain months 1–12; 2026 contains months 1–4. |
| `country` | Name of sovereign country observed | Text / Categorical (`str`) | `United States` | N/A | N/A | 10 distinct countries: Australia, Brazil, Canada, China, Germany, India, Nigeria, Pakistan, United Kingdom, United States. (136 records each). |
| `region` | Geographic continental region | Text / Categorical (`str`) | `North America` | N/A | N/A | 6 regions: Africa (136), Asia (408), Europe (272), North America (272), Oceania (136), South America (136). |
| `student_ai_usage_pct` | Percentage of surveyed students actively utilizing AI tools | Integer / Percentage (`int64`) | `10` | `0%` | `65%` | Overall dataset mean: 30.99%. |
| `teacher_ai_usage_pct` | Percentage of surveyed educators/teachers utilizing AI tools | Integer / Percentage (`int64`) | `8` | `0%` | `60%` | Overall dataset mean: 29.91%. |
| `schools_ai_adoption_pct` | Percentage of educational institutions with formal AI adoption | Integer / Percentage (`int64`) | `5` | `0%` | `62%` | Overall dataset mean: 29.42%. |
| `avg_daily_ai_usage_min` | Average daily time spent utilizing AI educational tools in minutes | Integer / Time (`int64`) | `29` | `5 min` | `60 min` | Overall dataset mean: 32.82 minutes. |
| `top_ai_tool` | Leading AI platform reported for the country-month observation | Text / Categorical (`str`) | `ChatGPT` | N/A | N/A | 4 distinct tools: ChatGPT (363 records, 26.69%), Microsoft Copilot (341 records, 25.07%), Google Gemini (330 records, 24.26%), Khanmigo (326 records, 23.97%). |
| `internet_penetration_pct` | National internet connectivity penetration rate | Integer / Percentage (`int64`) | `90` | `42%` | `96%` | Fixed per country in dataset (e.g., Nigeria: 42%, Pakistan: 45%, India: 50%, China: 70%, Brazil: 75%, US: 90%, UK: 92%, Germany: 93%, Canada: 94%, Australia: 96%). Overall mean: 74.70%. |
| `education_index` | Composite Education Index score (UNDP standard scale 0.0 to 1.0) | Float (`float64`) | `0.90` | `0.52` | `0.94` | Country-level benchmark metric. Overall mean: 0.78. |
| `government_ai_policy` | National governmental policy status regarding AI in education | Categorical (`str`) | `Active` | N/A | N/A | 3 states: `Active` (474 records), `Draft` (444 records), `None` (442 records). **Critical Note:** Literal string `"None"` must be preserved and not parsed as a null/missing value in data pipelines. |
| `urban_ai_usage_pct` | Percentage of students/schools in urban centers adopting AI | Integer / Percentage (`int64`) | `12` | `0%` | `70%` | Overall dataset mean: 33.57%. |
| `rural_ai_usage_pct` | Percentage of students/schools in rural districts adopting AI | Integer / Percentage (`int64`) | `4` | `0%` | `59%` | Overall dataset mean: 21.60%. |
| `ai_in_curriculum` | Formal integration of AI topics into the official educational curriculum | Categorical (`str`) | `Yes` | N/A | N/A | Binary status: `Yes` (687 records, 50.51%), `No` (673 records, 49.49%). |
| `gender_gap_ai_usage_pct` | Difference in adoption percentage between male and female cohorts | Integer / Percentage (`int64`) | `4` | `1%` | `10%` | Overall dataset mean: 5.41%. |

---

## 2. Engineered / Derived Features (in Processed Dataset)

| Derived Column | Description | Data Type | Derivation Logic | Example | Analytical Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `date` | Standardized ISO-8601 month start timestamp | Datetime (`datetime64[ns]`) | `YYYY-MM-01` from `year` and `month` | `2015-01-01` | Enables native Tableau date hierarchies, continuous timelines, and multi-year forecasting. |
| `urban_rural_gap_pct` | Absolute disparity between urban and rural adoption | Integer / Float (`float64`) | `urban_ai_usage_pct` - `rural_ai_usage_pct` | `8.0` | Quantifies the digital access divide in education across regions over time (Mean: 11.97%). |
| `student_teacher_diff_pct` | Net adoption gap between students and teachers | Integer / Float (`float64`) | `student_ai_usage_pct` - `teacher_ai_usage_pct` | `2.0` | Identifies whether student grassroots adoption outpaces institutional educator readiness (Mean: +1.08%). |
| `student_teacher_ratio` | Ratio of student adoption rate to teacher adoption rate | Float (`float64`) | `student_ai_usage_pct / max(teacher_ai_usage_pct, 1)` | `1.25` | Normalized relative measure of user parity in classrooms. |

---

## 3. Data Integrity & Quality Verification Summary

- **Total Missing Values:** `0` (Zero missing entries across all 16 raw columns upon proper handling of the `"None"` category).
- **Duplicate Records:** `0` (Zero duplicate tuples identified).
- **Outliers / Range Violations:** Zero percentages out of `[0, 100]` range; Education Index strictly bounded between `0.52` and `0.94`.
- **Temporal Completeness:** Full monthly continuity for all 10 countries across 136 consecutive months from Jan 2015 to Apr 2026.
