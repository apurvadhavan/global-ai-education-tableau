# Project Methodology & Analytical Workflow

**Project Title:** Global AI Adoption in Education: A Comprehensive Global Analysis  
**Course:** Data Analytics with Tableau Capstone Project  
**Tech Stack:** Python 3, Pandas, Tableau Desktop / Public, Flask, HTML5, CSS3, JavaScript  

---

## 1. End-to-End Workflow Architecture

The project adheres to an institutional-grade, multi-stage data analytics lifecycle:

```
┌───────────────────────────┐
│   1. Data Collection      │ ➔ 1,360 Monthly Observations (2015–2026) across 10 Countries
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│    2. Data Cleaning       │ ➔ Schema audit, 0 nulls verified, "None" policy string preservation
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│  3. Data Preparation      │ ➔ Feature engineering: ISO date, divide gaps, student-teacher ratios
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ 4. Exploratory Analysis   │ ➔ 16-dimensional statistical profiling via Jupyter Notebook
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ 5. Tableau Visualizations │ ➔ 14 analytical worksheets mapped to stakeholder questions
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│   6. Interactive Dashboard│ ➔ Executive KPI cards, regional maps, tool distribution, filters
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│  7. Guided Tableau Story  │ ➔ 6 structured narrative scenes tailored to 3 persona scenarios
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│   8. Performance Testing  │ ➔ Execution latency, render efficiency, calculation optimization
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│  9. Tableau Publishing    │ ➔ Publishing workbook to Tableau Public with clean web extracts
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ 10. Flask Web Integration │ ➔ Modular web portal embedding published Dashboard and Story
└───────────────────────────┘
```

---

## 2. Detailed Step-by-Step Methodology

### Phase 1: Data Collection & Extraction
- **Dataset Identification:** `Global AI in Education.csv` containing longitudinal survey and institutional adoption records.
- **Coverage:** 10 nations across 6 continents:
  - North America: United States, Canada
  - Europe: United Kingdom, Germany
  - Asia: China, India, Pakistan
  - South America: Brazil
  - Africa: Nigeria
  - Oceania: Australia
- **Time Horizon:** 136 distinct month periods from January 2015 through April 2026 (12 years of progression).

### Phase 2: Data Cleaning & Integrity Audit
A rigorous automated audit was implemented to ensure 100% data fidelity:
1. **Missing Value Audit:** All 16 columns were inspected. Standard pandas loaders convert the literal string `"None"` in `government_ai_policy` into `NaN`. Our workflow explicitly preserved `"None"` as a distinct categorical state indicating absence of formal national AI policy (442 occurrences).
2. **Duplicate Detection:** 0 duplicate rows were identified across all 1,360 observations.
3. **Range & Type Validation:** Percentage fields (`student_ai_usage_pct`, `teacher_ai_usage_pct`, etc.) were validated within $[0, 100]$. `education_index` was verified within $[0.52, 0.94]$.

### Phase 3: Data Preparation & Feature Engineering
- Generated a continuous ISO-8601 timeline column: `date` (`YYYY-MM-01`) from `year` and `month` fields.
- Engineered analytical gap fields:
  - `urban_rural_gap_pct` = $\text{urban\_ai\_usage\_pct} - \text{rural\_ai\_usage\_pct}$ (Mean: $11.97\%$)
  - `student_teacher_diff_pct` = $\text{student\_ai\_usage\_pct} - \text{teacher\_ai\_usage\_pct}$ (Mean: $+1.08\%$)
  - `student_teacher_ratio` = $\text{student\_ai\_usage\_pct} / \max(\text{teacher\_ai\_usage\_pct}, 1)$
- Exported the enriched dataset to `data/processed/cleaned_ai_education.csv`.

### Phase 4: Exploratory Data Analysis (EDA)
- Implemented in `analysis/data_analysis.ipynb` across 16 thematic modules.
- Evaluated temporal velocity (from $4.98\%$ student adoption in 2015 to $60.75\%$ in 2026).
- Analyzed infrastructure divergence between developing economies (Nigeria: $42\%$ internet penetration) and mature economies (Australia: $96\%$).

### Phase 5: Tableau Visualization Design
Designed 14 focused worksheets answering analytical stakeholder questions:
1. Global choropleth map of AI adoption by country.
2. Regional multi-line trend comparison over time.
3. Student vs Teacher adoption scatter and dual-axis trajectories.
4. Institutional school adoption bar charts.
5. AI tool popularity breakdown across regions (ChatGPT, Copilot, Gemini, Khanmigo).
6. Internet penetration vs AI adoption correlation scatter plot.
7. Education Index vs AI usage regression plot.
8. Policy impact distribution (Active vs Draft vs None).
9. Urban vs Rural adoption divergence lines.
10. AI Curriculum inclusion impact box-and-whisker.
11. Gender gap boxplot and regional averages.
12. Daily usage minutes distribution and correlation with adoption.
13. Tool shift across time (2015–2026).
14. Net adoption gap trajectory.

### Phase 6: Executive Dashboard Construction
- **Canvas Dimensions:** Responsive fixed grid ($1200\text{px} \times 900\text{px}$) or automatic viewport sizing.
- **KPI Summary Cards:**
  - Average Student AI Usage: **30.99%**
  - Average Teacher AI Usage: **29.91%**
  - Average School AI Adoption: **29.42%**
  - Average Daily Usage: **32.82 min**
  - Average Internet Penetration: **74.70%**
  - Average Education Index: **0.78**
- **Interactive Controls & Global Filters:** Year, Region, Country, Top AI Tool, Government AI Policy, and AI in Curriculum.

### Phase 7: Tableau Story Construction
Created a 6-scene analytical narrative targeting three stakeholder personas:
- **Scene 1:** Global Overview (Global adoption growth from 2015 to 2026).
- **Scene 2:** Regional & Geographic Divergence (Disparities across the 6 global regions).
- **Scene 3:** The Classroom Gap (Students consistently outpacing teachers by +1.08%).
- **Scene 4:** Competitive AI Tool Landscape (ChatGPT leading at 26.69%, Copilot 25.07%, Gemini 24.26%, Khanmigo 23.97%).
- **Scene 5:** Infrastructure & Policy Realities (Why policy presence alone does not dictate adoption rate).
- **Scene 6:** Equity & The Digital Divide (The 11.97% urban-rural gap and persistent 5.41% gender gap).

### Phase 8: Performance Testing
- Monitored query performance and rendering response times.
- Documented in `documentation/performance_testing.md` with guidelines for Tableau Desktop Performance Recording.

### Phase 9: Tableau Public Publishing
- Created clean packaged workbook (`.twbx`) with data extract.
- Published to Tableau Public with client-side rendering enabled.
- Retrieved embed URLs for the Dashboard and Story.

### Phase 10: Flask Web Integration
- Built a modular Flask application structure (`app.py`, `templates/`, `static/`).
- Implemented responsive Tableau embed wrappers utilizing Tableau Embedding API v3.
- Configured dynamic fallback banners and live URL preview testers for instant configuration.
