# Performance Testing & Audit Guidelines

**Project Title:** Global AI Adoption in Education: A Comprehensive Global Analysis  
**Testing Subject:** Tableau Workbook Architecture & Flask Web Integration  
**Audit Status:** Baseline System Parameters Documented; Tableau Engine Benchmarks Require Manual Verification in Tableau Desktop.

---

## 1. Actual System & Dataset Parameters (Verified from Data)

The baseline parameters below are programmatically audited and verified from `cleaned_ai_education.csv`:

| Parameter | Actual Value | Verification Source |
| :--- | :--- | :--- |
| **Number of Records Loaded** | **1,360 rows** | Direct programmatic row count (`df.shape[0]`) |
| **Raw Column Count** | **16 columns** | Schema inspection of source CSV |
| **Processed Column Count** | **20 columns** | Schema inspection of cleaned CSV |
| **Number of Calculated Fields** | **4 fields** | Python pipeline (`date`, `urban_rural_gap_pct`, `student_teacher_diff_pct`, `student_teacher_ratio`) |
| **Dataset File Size** | **~138 KB** | Compact flat file extract |
| **Recommended Dashboard Filters** | **6 global filters** | `year`, `region`, `country`, `top_ai_tool`, `government_ai_policy`, `ai_in_curriculum` |
| **Recommended Visualizations** | **5–6 core worksheets** | Recommended visualization plan in `tableau/README.md` |
| **Recommended Story Scenes** | **4 narrative scenes** | Recommended story plan in `tableau/README.md` |

---

## 2. Tableau Performance Metrics Requiring Manual Desktop Verification

> [!IMPORTANT]
> **Data Integrity Rule:** Actual rendering times, query compilation durations, and graphical execution latencies cannot be simulated or fabricated programmatically outside of the native Tableau Desktop engine.
>
> In accordance with Skillwallet evaluation requirements, the items below must be measured manually in Tableau Desktop using the **Tableau Performance Recorder**.

| Performance Metric | Expected Target | Measurement Status |
| :--- | :--- | :--- |
| **Extract Query Latency** | $< 50\text{ ms}$ | *Requires manual verification in Tableau Desktop* |
| **Initial Dashboard Render Time** | $< 2.0\text{ s}$ | *Requires manual verification in Tableau Desktop* |
| **Global Filter Refresh Latency** | $< 300\text{ ms}$ | *Requires manual verification in Tableau Desktop* |
| **Story Scene Transition Latency** | $< 500\text{ ms}$ | *Requires manual verification in Tableau Desktop* |
| **Client-Side Web Viewport Scaling**| Responsive | *Verified in Flask Web Integration* |

---

## 3. Step-by-Step Instructions to Run the Tableau Performance Recorder

To capture authentic execution and query benchmarks for your final capstone evaluation:

1. Launch **Tableau Desktop**.
2. From the top application menu bar, select:
   **Help** ➔ **Settings and Performance** ➔ **Start Performance Recording**.
3. Open your workbook: `tableau/Global_AI_Adoption.twbx`.
4. Perform typical user interactions:
   - Select the **Dashboard** tab.
   - Adjust the **Year** filter slider from `2015` to `2026`.
   - Toggle the **Region** filter between `All`, `Asia`, and `Europe`.
   - Click through all narrative scenes in the **Story** tab.
5. Return to the application menu and select:
   **Help** ➔ **Settings and Performance** ➔ **Stop Performance Recording**.
6. Tableau will automatically compile and open a dedicated **Performance Summary Workbook** displaying:
   - Chronological timeline of visual events (`Executing Query`, `Computing Layout`, `Rendering Marks`).
   - Query execution times by worksheet.
   - Identification of any calculation or query bottlenecks.
7. Save a screenshot or note the elapsed rendering times to include in your final demonstration video and documentation.

---

## 4. Built-in Optimization Best Practices

1. **Pre-Materialized Analytical Fields:**
   - Calculations such as continuous date generation (`date`) and gap metrics (`urban_rural_gap_pct`) were computed during data preparation in Python, eliminating on-the-fly string parsing overhead (`DATEPARSE`) in Tableau.
2. **Columnar Data Extract (`.hyper`):**
   - Utilizing an Extract connection stores data in Tableau's columnar format, avoiding disk I/O bottlenecks.
3. **Low-Cardinality Filter Domains:**
   - Categorical filters (Region: 6 values, Tool: 4 values, Policy: 3 values, Curriculum: 2 values) operate on indexed domains, minimizing filter tree evaluation costs.
