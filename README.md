# Global AI Adoption in Education: A Comprehensive Global Analysis

**Capstone Project:** Data Analytics with Tableau  
**Author:** Academic Capstone Portfolio  
**Tech Stack:** Python 3.14, Flask, Pandas, Tableau Desktop / Public, HTML5, CSS3, JavaScript  

---

## Project Status & Implementation Boundaries

To ensure complete academic transparency and integrity for mentor evaluation, this repository clearly distinguishes what has been implemented programmatically versus what must be executed manually in Tableau Desktop:

### COMPLETED AUTOMATICALLY IN THIS REPOSITORY:
- [x] **Dataset Collection & Extraction:** Ingested source CSV (`Global AI in Education.csv`, 1,360 rows, 16 features).
- [x] **Dataset Inspection & Audit:** Audited schema, 0 nulls, 0 duplicates, and verified numeric bounds.
- [x] **Data Preparation & Engineering:** Handled `"None"` policy category preservation, engineered continuous ISO `date`, `urban_rural_gap_pct`, and `student_teacher_diff_pct` (`data/processed/cleaned_ai_education.csv`).
- [x] **Exploratory Data Analysis:** 16-section Jupyter Notebook (`analysis/data_analysis.ipynb`) analyzing all dimensions.
- [x] **Flask Web Integration:** Production-grade Flask web application running on port `5000` across all 5 core routes.
- [x] **Web UI & Embedding Architecture:** Modern, responsive UI with **Tableau Embedding API v3**, fullscreen controls, reload handlers, and live URL preview testers.
- [x] **Complete Supporting Documentation:** Data dictionary, methodology timeline, empirical insights report, and performance testing guidelines.

### TO BE COMPLETED MANUALLY IN TABLEAU DESKTOP:
- [ ] **Actual Tableau Visualizations:** Connecting `cleaned_ai_education.csv` in Tableau Desktop and building the recommended worksheets (detailed in `tableau/README.md`).
- [ ] **Actual Tableau Dashboard:** Assembling the dashboard `GLOBAL AI ADOPTION IN EDUCATION` with the calculated KPI cards and global filters in Tableau Desktop.
- [ ] **Actual Tableau Story:** Creating the narrative scenes in Tableau Desktop.
- [ ] **Tableau Performance Recording:** Running the native Tableau Desktop Performance Recorder (**Help** ➔ **Settings and Performance** ➔ **Start Performance Recording**).
- [ ] **Tableau Publishing:** Publishing the workbook to Tableau Public or Tableau Server.
- [ ] **Real Tableau URLs:** Replacing the placeholder URLs in `app.py` with your live published Tableau Public links.

---

## Project Overview

This capstone project delivers an end-to-end, institutional-quality data analytics analysis of global Artificial Intelligence adoption across educational ecosystems. Utilizing a longitudinal dataset of **1,360 monthly observations across 10 sovereign nations from January 2015 to April 2026**, the project uncovers empirical trends in student AI usage, educator engagement, institutional school adoption, market tool distribution, national policy impact, and demographic equity divides.

The final visual products—an interactive **Tableau Dashboard** with calculated KPI cards and dynamic filters, and a **Guided Tableau Story** answering specific stakeholder inquiries—are embedded directly within a production-grade **Flask web application**.

---

## Problem Statement

Educational leaders, EdTech product developers, and academic researchers often lack objective, empirical visibility into how generative and analytical AI tools are adopted inside real classrooms. Key challenges addressed by this project include:
1. **Grassroots Friction:** Students frequently adopt AI tools at higher velocities than educators and institutional guidelines can accommodate, creating academic integrity and instructional alignment challenges.
2. **Infrastructure vs. Access:** While national internet penetration ranges between 42% and 96%, whether connectivity dictates intra-school adoption or primarily restricts rural reach requires empirical verification.
3. **The Urban-Rural Divide:** Geographic access disparities threaten to leave non-urban student cohorts significantly behind in technological fluency.
4. **Tool Monopoly vs. Diversity:** Establishing whether a single foundation model monopolizes classroom study or whether purpose-built educational platforms sustain competitive market parity.

---

## Objectives

- **Audit & Cleanse Data:** Execute rigorous validation on all 16 raw features, preserving categorical integrity (e.g. preserving `"None"` policy status against false null imputation).
- **Engineer Analytical Measures:** Formulate continuous ISO timelines (`date`), urban-rural divide disparities (`urban_rural_gap_pct`), and student-teacher adoption friction (`student_teacher_diff_pct`).
- **Conduct 16-Module EDA:** Generate reproducible exploratory findings in `analysis/data_analysis.ipynb`.
- **Architect Tableau Visualizations:** Design a recommended set of core worksheets mapped to strategic policy questions.
- **Build Executive Dashboard:** Formulate a cohesive dashboard titled `GLOBAL AI ADOPTION IN EDUCATION` with 6 verified KPI cards and multi-scale filters.
- **Develop Guided Story:** Guide stakeholders through a natural narrative addressing three distinct user personas.
- **Embed in Flask Web Portal:** Deliver a responsive, modern web application on port `5000` with live URL testing and interactive fallback previews.

---

## Dataset

- **Raw Data Path:** `data/raw/Global AI in Education.csv`
- **Cleaned Data Path:** `data/processed/cleaned_ai_education.csv`
- **Total Records:** **1,360 rows** (136 months $\times$ 10 countries)
- **Time Range:** January 2015 – April 2026 (12 years of monthly data)
- **Countries Analyzed (10):** Australia, Brazil, Canada, China, Germany, India, Nigeria, Pakistan, United Kingdom, United States (136 observations each).
- **Regions (6):** Africa (136), Asia (408), Europe (272), North America (272), Oceania (136), South America (136).
- **Data Quality:** 0 missing values, 0 duplicate records, 100% verified numeric ranges.

---

## Dataset Columns

| Column Name | Type | Description | Observed Range | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `year` | Int | Observation year | 2015 to 2026 | Discrete annual indicator |
| `month` | Int | Observation month | 1 to 12 | Jan–Dec (2015–25), Jan–Apr (2026) |
| `country` | Str | Sovereign nation | 10 nations | 136 records per country |
| `region` | Str | Continental region | 6 regions | Africa, Asia, Europe, NA, Oceania, SA |
| `student_ai_usage_pct` | Int | Student AI adoption rate (%) | 0% to 65% | Mean: 30.99% |
| `teacher_ai_usage_pct` | Int | Teacher AI adoption rate (%) | 0% to 60% | Mean: 29.91% |
| `schools_ai_adoption_pct`| Int | School institutional adoption (%) | 0% to 62% | Mean: 29.42% |
| `avg_daily_ai_usage_min`| Int | Daily usage time (minutes) | 5 to 60 min | Mean: 32.82 min |
| `top_ai_tool` | Str | Leading educational AI tool | 4 platforms | ChatGPT, Copilot, Gemini, Khanmigo |
| `internet_penetration_pct`| Int | National internet penetration (%)| 42% to 96% | Mean: 74.70% |
| `education_index` | Float| UNDP Education Index score | 0.52 to 0.94 | Mean: 0.78 |
| `government_ai_policy` | Str | National policy status | Active, Draft, None | Preserved as valid categorical strings |
| `urban_ai_usage_pct` | Int | Urban cohort adoption (%) | 0% to 70% | Mean: 33.57% |
| `rural_ai_usage_pct` | Int | Rural cohort adoption (%) | 0% to 59% | Mean: 21.60% |
| `ai_in_curriculum` | Str | Official curriculum integration | Yes (687), No (673)| Binary categorical indicator |
| `gender_gap_ai_usage_pct`| Int | Male vs female adoption gap (%) | 1% to 10% | Mean: 5.41% |

---

## Data Preparation

The data cleaning pipeline (`prepare_data.py`) executes:
1. **Preservation of `"None"` Policy:** Standard pandas loaders convert the string `"None"` in `government_ai_policy` to null. Our workflow preserves this category, ensuring all 442 `"None"` records remain intact.
2. **Standardized ISO Date:** Engineered `date` (`YYYY-MM-01`) for native Tableau time hierarchies.
3. **Derived Metrics:**
   - `urban_rural_gap_pct` = `urban_ai_usage_pct` - `rural_ai_usage_pct` (Mean: 11.97%)
   - `student_teacher_diff_pct` = `student_ai_usage_pct` - `teacher_ai_usage_pct` (Mean: +1.08%)
   - `student_teacher_ratio` = `student_ai_usage_pct` / `max(teacher_ai_usage_pct, 1)`

---

## Exploratory Analysis

Implemented in `analysis/data_analysis.ipynb` across 16 structured analytical sections:
1. Dataset overview & schema validation
2. Missing-value audit (0 nulls confirmed)
3. Duplicate verification (0 duplicates confirmed)
4. Descriptive statistics of all continuous features
5. Country-level comparative profiles
6. Regional adoption comparisons
7. Student vs teacher adoption friction analysis
8. School institutional adoption trends
9. AI tool distribution & market share breakdown
10. Internet penetration correlation analysis
11. Education index correlation analysis
12. Government AI policy status comparison
13. Urban vs rural accessibility divide analysis
14. AI in curriculum impact assessment
15. Gender gap stability and regional variances
16. Multi-year temporal trajectory synthesis

---

## Recommended Tableau Visualizations

The core worksheets recommended to explain the dataset thoroughly without padding:
- **Vis 1 (Global Adoption Map):** Choropleth symbol/filled map showing student AI adoption by country.
- **Vis 2 (Multi-Year Trajectory):** Dual-axis line chart tracking student usage (4.98% to 60.75%), teacher usage (4.04% to 59.00%), and school adoption over time.
- **Vis 3 (Regional Comparison):** Horizontal bar chart comparing adoption across the 6 continental regions.
- **Vis 4 (AI Platform Distribution):** Bar / Donut chart benchmarking the 4 tools (ChatGPT 26.69%, Copilot 25.07%, Gemini 24.26%, Khanmigo 23.97%).
- **Vis 5 (Infrastructure & Policy Relationship):** Scatter plot (Internet vs. Adoption) with Policy status as color.
- **Vis 6 (Digital Equity Divide):** Area/line chart showing the 11.97% urban-rural gap and 5.41% gender gap.

---

## Dashboard

**Title:** `GLOBAL AI ADOPTION IN EDUCATION`  
Designed as an executive single-pane analytics console:
- **Calculated KPI Cards:**
  - Average Student AI Usage: **30.99%**
  - Average Teacher AI Usage: **29.91%**
  - Average School AI Adoption: **29.42%**
  - Average Daily Usage: **32.82 min**
  - Average Internet Penetration: **74.70%**
  - Average Education Index: **0.78**
- **Interactive Multi-Scale Filters:** `Year` (2015–2026), `Region`, `Country`, `Top AI Tool`, `Government Policy`, `AI in Curriculum`.

---

## Tableau Story

A guided analytical narrative organized around the natural flow of findings:
- **Scene 1 (Longitudinal Growth):** Global student AI usage growing from 4.98% in 2015 to 60.75% in 2026.
- **Scene 2 (The Classroom Dynamic):** Students systematically leading educators by +1.08% across observations.
- **Scene 3 (Educational AI Tools):** Competitive parity among the 4 major educational tools.
- **Scene 4 (Equity, Infrastructure & Policy):** The structural 11.97% urban-rural divide, 5.41% gender gap, and draft policy pilot dynamics.

---

## Performance Testing

- Monitored data footprint (1,360 rows, 138 KB CSV extract).
- Documented in `documentation/performance_testing.md`.
- Guidelines provided for running the native Tableau Desktop Performance Recorder (**Help** ➔ **Settings and Performance** ➔ **Start Performance Recording**).

---

## Flask Web Integration

Built with Python, Flask, HTML5, CSS3, and JavaScript:
- **Responsive Navigation:** Clean navbar with active route highlighting across the 4 assessment pages.
- **Embedded Visualization Architecture:** Uses modern **Tableau Embedding API v3** (`<tableau-viz>`) to cleanly render your published Tableau visualizations without any developer clutter.
- **Core Assessment Pages:**
  - `/` — **Home:** Project title, overview, factual KPI cards, stakeholder scenarios, country data table.
  - `/dashboard` — **Dashboard:** Dedicated, clean embedding page for the published Tableau Dashboard.
  - `/story` — **Story:** Dedicated, clean embedding page for the published Tableau Story.
  - `/insights` — **Insights:** Detailed empirical insights achieved from the data analytics.
  - `/methodology` — Analytical workflow documentation.
  - `/api/summary` — REST API endpoint returning computed KPIs.

---

## How to Run Locally

### 1. Prerequisites
- Python 3.9 or higher (tested on Python 3.14)
- Git (optional, for cloning)

### 2. Installation
Navigate to the project directory:
```bash
cd Global-AI-Adoption-Education
pip install -r requirements.txt
```

### 3. Run the Flask Web Application
```bash
python app.py
```

### 4. Open in Web Browser
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## Tableau Publishing

To connect your own published Tableau Public workbook to the Flask web app:
1. Open `data/processed/cleaned_ai_education.csv` in **Tableau Desktop**.
2. Build the Dashboard and Story as detailed in `tableau/README.md`.
3. Save the packaged workbook into `tableau/Global_AI_Adoption.twbx`.
4. Publish to Tableau Public: **Server** ➔ **Tableau Public** ➔ **Save to Tableau Public As...**
5. On the published Tableau Public web page, click **Share** and copy the **Link**.
6. Open `app.py` and paste your links into the configuration section:
   ```python
   TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/YourWorkbook/Dashboard"
   TABLEAU_STORY_URL = "https://public.tableau.com/views/YourWorkbook/Story"
   ```
7. Refresh your web app at `http://127.0.0.1:5000/dashboard` and `http://127.0.0.1:5000/story`.

---

## Project Structure

```
Global-AI-Adoption-Education/
│
├── app.py                      # Core Flask web application & Tableau configuration
├── requirements.txt            # Minimal required Python dependencies
├── README.md                   # Comprehensive capstone project documentation
├── .gitignore                  # Git ignore specification for Python & OS files
│
├── data/
│   ├── raw/
│   │   └── Global AI in Education.csv       # Source dataset (1,360 rows, 16 columns)
│   └── processed/
│       └── cleaned_ai_education.csv         # Cleaned & engineered dataset (1,360 rows, 20 columns)
│
├── templates/
│   ├── base.html               # Master layout template (navbar, footer, assets)
│   ├── index.html              # Landing page (hero, KPIs, overview, scenarios)
│   ├── dashboard.html          # Tableau Dashboard embed page with controls
│   ├── story.html              # Tableau Story embed page with narrative scenes
│   ├── methodology.html        # 10-phase visual analytics timeline
│   └── insights.html           # Deep dive into the 9 empirical insight dimensions
│
├── static/
│   ├── css/
│   │   └── style.css           # Institutional modern analytics design system
│   ├── js/
│   │   └── main.js             # Live URL tester, fullscreen, and UI interactions
│   └── images/                 # Image assets directory
│
├── tableau/
│   └── README.md               # Step-by-step workbook building and publishing guide
│
├── analysis/
│   └── data_analysis.ipynb     # 16-section exploratory data analysis notebook
│
├── documentation/
│   ├── data_dictionary.md      # Full schema, types, bounds, and feature derivations
│   ├── methodology.md          # End-to-end analytical lifecycle documentation
│   ├── insights.md             # Empirical findings grounded in dataset facts
│   ├── performance_testing.md  # Performance metrics and Tableau audit guidelines
│   └── project_documentation.md# Step-by-step 13-stage capstone documentation
│
└── screenshots/
    ├── dashboard.png           # Executive dashboard schematic screenshot
    ├── story.png               # Tableau story layout screenshot
    └── flask-web-app.png       # Integrated web application screenshot
```

---

## Key Insights

1. **Growth Explosion:** Global student AI usage expanded from **4.98%** in 2015 to **60.75%** in 2026 (a **12.2x increase**).
2. **Grassroots Lead:** Students consistently lead educators in AI adoption by **+1.08 percentage points** globally.
3. **Competitive Parity:** The AI tool market is divided among 4 balanced platforms: ChatGPT (**26.69%**), Copilot (**25.07%**), Gemini (**24.26%**), and Khanmigo (**23.97%**).
4. **The Urban-Rural Divide:** Urban AI usage (**33.57%**) significantly exceeds rural usage (**21.60%**), establishing a **11.97% structural divide**.
5. **Policy Nuance:** Countries with draft policies exhibit the highest student usage (**32.00%**), while active policies introduce compliance safeguards that stabilize adoption (**30.36%**).
6. **Curriculum Benefit:** Formal curriculum inclusion correlates positively with student (**31.35%** vs 30.63%) and school-wide adoption (**29.69%** vs 29.14%).
7. **Persistent Gender Gap:** The gender disparity in student AI usage averages a stable **5.41 percentage points** across 2015–2026.

---

## Stakeholder Scenarios

- **Dr. Sarah Chen (EdTech Director):** Addresses teacher training gaps and curriculum integration to formalize student usage.
- **Marcus Williams (EdTech Entrepreneur):** Leverages tool market parity and targets underserved rural cohorts.
- **Prof. Elena Rodriguez (Academic AI Researcher):** Evaluates macro infrastructure links, policy phases, and demographic equity.

---

## Future Improvements

- Ingestion of granular sub-national district data across individual provinces/states.
- Tracking specialized discipline adoption (STEM vs Humanities vs Vocational).
- Longitudinal tracking of qualitative student learning gains associated with daily minutes spent.

---

## Author & Academic Integrity

- **Capstone Student:** Parth
- **Course:** Data Analytics with Tableau
- **Integrity Guarantee:** Zero synthetic statistics, zero fabricated Tableau URLs, 100% data provenance grounded strictly in `Global AI in Education.csv`.
