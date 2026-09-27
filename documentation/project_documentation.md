# Global AI Adoption in Education: Step-by-Step Project Documentation

**Project Title:** Global AI Adoption in Education: A Comprehensive Global Analysis  
**Curriculum Track:** Data Analytics with Tableau Capstone  
**Dataset:** `Global AI in Education.csv` (1,360 rows, 16 features)  
**Status:** Complete Implementation & Verified Delivery  

---

## Step 1: Dataset Collection
The raw dataset `Global AI in Education.csv` was ingested into `data/raw/Global AI in Education.csv`. It comprises **1,360 monthly country-level observations** covering 10 sovereign nations (Australia, Brazil, Canada, China, Germany, India, Nigeria, Pakistan, United Kingdom, United States) across a 12-year longitudinal span from **January 2015 to April 2026** (136 monthly records per country).

---

## Step 2: Dataset Inspection
Programmatic audit via Python and pandas revealed:
- **Shape:** 1,360 rows, 16 raw features.
- **Completeness:** 0 missing values across all columns upon proper handling of the `"None"` category.
- **Uniqueness:** 0 duplicate rows detected.
- **Critical Finding:** In `government_ai_policy`, standard pandas loading converts the string category `"None"` into `NaN`. We explicitly preserved `"None"` as a distinct categorical state indicating the absence of national AI policy (442 observations).

---

## Step 3: Data Cleaning & Preparation
Automated via `prepare_data.py`:
1. Preserved `"None"` policy status.
2. Standardized temporal feature into an ISO-8601 date column: `date` (`YYYY-MM-01`).
3. Formulated derived analytical features:
   - `urban_rural_gap_pct` = `urban_ai_usage_pct` - `rural_ai_usage_pct` (Mean: 11.97%)
   - `student_teacher_diff_pct` = `student_ai_usage_pct` - `teacher_ai_usage_pct` (Mean: +1.08%)
   - `student_teacher_ratio` = `student_ai_usage_pct` / `max(teacher_ai_usage_pct, 1)`
4. Saved cleaned file to `data/processed/cleaned_ai_education.csv` (1,360 rows, 20 features).

---

## Step 4: Tableau Connection
1. Launch **Tableau Desktop** (or Tableau Public Desktop edition).
2. Connect to Text File: `data/processed/cleaned_ai_education.csv`.
3. Set Connection to **Extract** (`.hyper` format).
4. Verify `date` is recognized as a Date, and percentage measures are whole numbers.

---

## Step 5: Visualization Creation (Recommended Core Worksheets)
Rather than creating arbitrary worksheets, the following focused set is recommended:
- **Vis 1 (Global Adoption Map):** Choropleth symbol/filled map showing student AI adoption by country.
- **Vis 2 (Multi-Year Trajectory):** Dual-axis line chart tracking student usage (4.98% to 60.75%), teacher usage (4.04% to 59.00%), and school adoption over time.
- **Vis 3 (Regional Comparison):** Horizontal bar chart comparing adoption across the 6 continental regions.
- **Vis 4 (AI Platform Distribution):** Bar / Donut chart benchmarking the 4 tools (ChatGPT 26.69%, Copilot 25.07%, Gemini 24.26%, Khanmigo 23.97%).
- **Vis 5 (Infrastructure & Policy Relationship):** Scatter plot (Internet vs. Adoption) with Policy status as color.
- **Vis 6 (Digital Equity Divide):** Area/line chart showing the 11.97% urban-rural gap and 5.41% gender gap.

---

## Step 6: Dashboard Creation
1. Open a new Dashboard tab named `GLOBAL AI ADOPTION IN EDUCATION`.
2. Configure layout dimensions (Responsive / 1200 x 900 px).
3. Place **Top KPI Cards** calculated from data:
   - Avg Student AI Usage: **30.99%**
   - Avg Teacher AI Usage: **29.91%**
   - Avg School Adoption: **29.42%**
   - Avg Daily Time: **32.82 min**
   - Avg Internet Penetration: **74.70%**
   - Avg Education Index: **0.78**
4. Position the core visualizations (Map, Trajectory, Tool Breakdown, Divide).
5. Add **Interactive Global Filters**: Year, Region, Country, Tool, Policy, Curriculum. Set filters to **"Apply to All Worksheets Using This Data Source"**.

---

## Step 7: Story Creation
Create a guided Tableau Story with a natural narrative arc:
- **Scene 1 (Longitudinal Growth):** Global student AI usage growing from 4.98% in 2015 to 60.75% in 2026.
- **Scene 2 (The Classroom Dynamic):** Students systematically leading educators by +1.08% across observations.
- **Scene 3 (Educational AI Tools):** Competitive parity among the 4 major educational tools.
- **Scene 4 (Equity, Infrastructure & Policy):** The structural 11.97% urban-rural divide, 5.41% gender gap, and draft policy pilot dynamics.

---

## Step 8: Performance Testing
1. In Tableau Desktop, enable **Help** ➔ **Settings and Performance** ➔ **Start Performance Recording**.
2. Interact with the Dashboard (adjust Year slider, toggle Region filters, navigate Story scenes).
3. Select **Stop Performance Recording** to view the performance summary.
4. Record actual query and render times in `documentation/performance_testing.md`.

---

## Step 9: Tableau Publishing
1. From Tableau Desktop, navigate to: **Server** ➔ **Tableau Public** ➔ **Save to Tableau Public As...**
2. Name the workbook: `Global AI Adoption in Education`.
3. Copy the published share link for the **Dashboard** and **Story**.

---

## Step 10: Flask Integration
1. Open `app.py`.
2. Replace the placeholder constants with your real published links:
   ```python
   TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/YourWorkbook/Dashboard"
   TABLEAU_STORY_URL = "https://public.tableau.com/views/YourWorkbook/Story"
   ```
3. The Flask templates (`dashboard.html` and `story.html`) will automatically mount your live visual products via **Tableau Embedding API v3**.

---

## Step 11: Local Testing
1. Run `python test_app.py` to verify that all endpoints respond with HTTP 200 OK.
2. Start the local server:
   ```bash
   python app.py
   ```
3. Navigate to `http://127.0.0.1:5000/` and verify:
   - Homepage overview, KPIs, and stakeholder scenarios.
   - Dashboard embedding with live URL preview testing.
   - Story embedding with narrative scene breakdown.
   - Methodology timeline and empirical Insights page.

---

## Step 12: GitHub Upload
Initialize Git in the `Global-AI-Adoption-Education` directory and push to GitHub:
```bash
cd Global-AI-Adoption-Education
git init
git add app.py requirements.txt README.md .gitignore
git add data/ templates/ static/ tableau/ analysis/ documentation/ screenshots/
git commit -m "feat: complete portfolio capstone project for Global AI Adoption in Education"
```

---

## Step 13: Final Demonstration (Video Presentation Guide)
Recommended 5–8 minute video structure:
1. **Introduction (1 min):** Project title, dataset scope (1,360 records, 10 countries, 12 years), and 3 stakeholder scenarios.
2. **Data Cleaning & EDA (1.5 min):** Data dictionary, schema audit (preserving `"None"` policy), and growth velocity (4.98% to 60.75%).
3. **Tableau Dashboard Demonstration (2 min):** Embedded dashboard in Flask, 6 KPI cards, and filter interaction.
4. **Tableau Story Walkthrough (1.5 min):** Core scenes showing student-teacher gap (+1.08%), tool shares, and the 11.97% urban-rural divide.
5. **Web Integration & Architecture (1 min):** Flask routing, responsiveness, and GitHub repository overview.
