# Tableau Workbook Implementation & Reference Guide

**Status:** Generated & Validated Tableau Workbook Available  
**Packaged Workbook (.twbx):** `tableau/Global_AI_Adoption.twbx`  
**XML Workbook (.twb):** `tableau/Global_AI_Adoption.twb`  
**Data Source:** `Global AI in Education.csv` (Packaged inside `.twbx` & linked in `tableau/Data/`)  

> [!NOTE]
> **Workbook Files Ready:** Both the packaged `.twbx` (self-contained with bundled CSV data) and the XML `.twb` file have been generated and validated against Tableau XML Schema specification version 18.1+. They are ready to be opened directly in Tableau Desktop or Tableau Public.

---

## 1. Connecting Tableau to the Dataset

1. Launch **Tableau Desktop** (or Tableau Public Desktop edition).
2. Under **Connect** (left panel), choose **Text file**.
3. Select `data/processed/cleaned_ai_education.csv`.
4. Verify the data schema:
   - `date` is recognized as a **Date** type (`YYYY-MM-01`).
   - `government_ai_policy` contains text categories (`Active`, `Draft`, `None`). Verify `None` is treated as a valid category, not a missing null.
   - All percentage columns (`student_ai_usage_pct`, etc.) are recognized as **Numbers (whole)**.
5. Set Connection to **Extract** to leverage Tableau's fast columnar data engine (`.hyper`).

---

## 2. Recommended Core Visualizations

Rather than creating arbitrary worksheets, the following set of visualizations answers all foundational questions raised by the dataset:

### Visualization 1: Global AI Adoption by Country
- **Purpose:** Provide an intuitive geographic overview of student adoption levels across all 10 analyzed countries.
- **Dataset Fields Used:** `country` (Dimension), `student_ai_usage_pct` (Measure - Average), `region` (Dimension).
- **Question Answered:** How does student AI usage vary across sovereign nations?
- **Recommended Tableau Chart Type:** **Choropleth (Symbol/Filled) Map**.

### Visualization 2: Multi-Year Adoption Trajectory (Students vs. Teachers vs. Schools)
- **Purpose:** Analyze adoption velocity and identify whether students lead or lag educators over time.
- **Dataset Fields Used:** `date` (Dimension - Continuous Month), `student_ai_usage_pct` (Average), `teacher_ai_usage_pct` (Average), `schools_ai_adoption_pct` (Average).
- **Question Answered:** How rapidly has AI adoption expanded from 2015 to 2026, and how does student uptake compare to teacher and institutional school adoption?
- **Recommended Tableau Chart Type:** **Multi-Line / Dual-Axis Line Chart**.

### Visualization 3: Regional Adoption Comparison
- **Purpose:** Compare adoption rates and classroom gaps across the 6 continental regions.
- **Dataset Fields Used:** `region` (Dimension), `student_ai_usage_pct` (Average), `teacher_ai_usage_pct` (Average).
- **Question Answered:** Which continental regions exhibit the highest adoption, and does adoption vary widely across continents?
- **Recommended Tableau Chart Type:** **Grouped Horizontal Bar Chart**.

### Visualization 4: AI Platform Popularity & Regional Share
- **Purpose:** Benchmark classroom platform leadership among ChatGPT, Microsoft Copilot, Google Gemini, and Khanmigo.
- **Dataset Fields Used:** `top_ai_tool` (Dimension), `region` (Dimension), `Number of Records` / Count.
- **Question Answered:** Which educational AI tools are most frequently reported as leading classroom study, and do specific regions prefer specific tools?
- **Recommended Tableau Chart Type:** **Grouped / 100% Stacked Bar Chart** or **Donut Chart**.

### Visualization 5: Infrastructure & Policy Relationships
- **Purpose:** Evaluate how national internet penetration, Education Index, and government policy status associate with adoption.
- **Dataset Fields Used:** `internet_penetration_pct` (Average), `education_index` (Average), `government_ai_policy` (Dimension), `student_ai_usage_pct` (Average).
- **Question Answered:** Do national internet connectivity and formal policy status dictate the rate of educational AI adoption?
- **Recommended Tableau Chart Type:** **Scatter Plot** (Internet vs. Adoption) with Policy as Color / Shape, or **Box & Whisker Plot** grouped by Policy.

### Visualization 6: Digital Equity & Accessibility (Urban vs. Rural & Gender Gap)
- **Purpose:** Quantify the two primary demographic divides present in the dataset.
- **Dataset Fields Used:** `date` (Dimension), `urban_ai_usage_pct` (Average), `rural_ai_usage_pct` (Average), `gender_gap_ai_usage_pct` (Average).
- **Question Answered:** What is the magnitude of the urban-rural access divide (11.97% gap) and gender disparity (5.41%) over time?
- **Recommended Tableau Chart Type:** **Dual-Area / Line Chart** (Urban vs. Rural over time) and **Bullet / Bar Chart** (Gender Gap by Region).

---

## 3. Recommended Dashboard Structure

**Title:** `GLOBAL AI ADOPTION IN EDUCATION`

Assemble the core worksheets into a single, cohesive dashboard prioritizing clarity:

1. **Top KPI Strip (Summary Cards):**
   - Average Student AI Usage: **30.99%**
   - Average Teacher AI Usage: **29.91%**
   - Average School Adoption: **29.42%**
   - Average Daily Time: **32.82 min**
   - Average Internet Penetration: **74.70%**
   - Average Education Index: **0.78**
2. **Main Analytics Grid:**
   - **Left / Center:** Global Adoption Map and Multi-Year Trajectory Line Chart.
   - **Right:** AI Tool Distribution and Urban vs. Rural Access Divide.
3. **Interactive Filter Panel:**
   - `Year` (Slider / Dropdown: 2015–2026)
   - `Region` (Multi-select dropdown)
   - `Country` (Multi-select dropdown)
   - `Top AI Tool` (Dropdown: ChatGPT, Copilot, Gemini, Khanmigo)
   - `Government AI Policy` (Dropdown: Active, Draft, None)
   - `AI in Curriculum` (Dropdown: Yes, No)
   - *Configuration:* Set filters to **"Apply to Worksheets ➔ All Using This Data Source"**.

---

## 4. Recommended Story Structure

Rather than forcing an arbitrary number of scenes, organize the story around the natural narrative arc of the findings:

- **Scene 1: Longitudinal Growth & Trajectory (2015–2026)**
  - *Focus:* A decade of expansion showing global student AI usage growing from **4.98%** in 2015 to **60.75%** in 2026.
- **Scene 2: The Classroom Dynamic (Students vs. Teachers)**
  - *Focus:* Grassroots student adoption leading educator institutional adoption by **+1.08%** across almost every observation period.
- **Scene 3: The Educational AI Tool Landscape**
  - *Focus:* Balanced competitive share among the 4 tools (ChatGPT 26.69%, Copilot 25.07%, Gemini 24.26%, Khanmigo 23.97%).
- **Scene 4: Infrastructure, Policy & Digital Equity**
  - *Focus:* Why policy in draft phase correlates with elevated pilot usage (32.00%), and the critical **11.97% urban-rural gap** and **5.41% gender gap**.

---

## 5. Saving the Workbook

1. In Tableau Desktop, choose **File** ➔ **Save As...**
2. Select **Tableau Packaged Workbook (*.twbx)**.
3. Save the file into this folder as:
   `tableau/Global_AI_Adoption.twbx`

---

## 6. Publishing to Tableau Public & Embedding in Flask

1. In Tableau Desktop, navigate to: **Server** ➔ **Tableau Public** ➔ **Save to Tableau Public As...**
2. Sign in with your Tableau Public account.
3. Name the workbook: `Global AI Adoption in Education`.
4. Once published, your default browser opens the visualization on Tableau Public.
5. Click **Share** (bottom toolbar), copy the **Link**, and paste into `app.py`:
   ```python
   TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/YourWorkbook/YourDashboard"
   TABLEAU_STORY_URL = "https://public.tableau.com/views/YourWorkbook/YourStory"
   ```
6. Open your Flask app at `http://127.0.0.1:5000/dashboard` and `http://127.0.0.1:5000/story` to verify the responsive live embed.
