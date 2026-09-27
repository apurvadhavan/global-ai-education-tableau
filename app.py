import os
from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# ==============================================================================
# TABLEAU CONFIGURATION
# ==============================================================================
# Paste your published Tableau Public or Tableau Server URLs below:
# Example:
# TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/GlobalAIInEducation/Dashboard"
# TABLEAU_STORY_URL = "https://public.tableau.com/views/GlobalAIInEducation/Story"
# ==============================================================================

TABLEAU_DASHBOARD_URL = os.environ.get(
    "TABLEAU_DASHBOARD_URL",
    "PASTE_TABLEAU_DASHBOARD_URL_HERE"
)

TABLEAU_STORY_URL = os.environ.get(
    "TABLEAU_STORY_URL",
    "PASTE_TABLEAU_STORY_URL_HERE"
)

# ==============================================================================
# DATASET COMPUTATION ENGINE (CSV SOURCE OF TRUTH)
# ==============================================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "cleaned_ai_education.csv")
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "Global AI in Education.csv")

def load_data():
    """Load dataset with high fidelity, preserving 'None' as category."""
    path = PROCESSED_DATA_PATH if os.path.exists(PROCESSED_DATA_PATH) else RAW_DATA_PATH
    return pd.read_csv(path, keep_default_na=False)

def get_kpis():
    """Calculate factual dataset KPIs strictly derived from CSV."""
    df = load_data()
    return {
        "total_records": int(len(df)),
        "total_countries": int(df["country"].nunique()),
        "total_regions": int(df["region"].nunique()),
        "year_min": int(df["year"].min()),
        "year_max": int(df["year"].max()),
        "avg_student_ai": round(float(df["student_ai_usage_pct"].mean()), 2),
        "avg_teacher_ai": round(float(df["teacher_ai_usage_pct"].mean()), 2),
        "avg_school_ai": round(float(df["schools_ai_adoption_pct"].mean()), 2),
        "avg_daily_min": round(float(df["avg_daily_ai_usage_min"].mean()), 2),
        "avg_internet": round(float(df["internet_penetration_pct"].mean()), 2),
        "avg_education_index": round(float(df["education_index"].mean()), 2),
        "avg_urban_ai": round(float(df["urban_ai_usage_pct"].mean()), 2),
        "avg_rural_ai": round(float(df["rural_ai_usage_pct"].mean()), 2),
        "urban_rural_gap": round(float(df["urban_ai_usage_pct"].mean() - df["rural_ai_usage_pct"].mean()), 2),
        "student_teacher_gap": round(float(df["student_ai_usage_pct"].mean() - df["teacher_ai_usage_pct"].mean()), 2),
        "avg_gender_gap": round(float(df["gender_gap_ai_usage_pct"].mean()), 2),
        "top_tools": df["top_ai_tool"].value_counts().to_dict(),
        "policy_counts": df["government_ai_policy"].value_counts().to_dict(),
        "curriculum_counts": df["ai_in_curriculum"].value_counts().to_dict(),
    }

@app.context_processor
def inject_globals():
    return {
        "TABLEAU_DASHBOARD_URL": TABLEAU_DASHBOARD_URL,
        "TABLEAU_STORY_URL": TABLEAU_STORY_URL,
        "has_dashboard_url": TABLEAU_DASHBOARD_URL.startswith("http"),
        "has_story_url": TABLEAU_STORY_URL.startswith("http"),
        "kpis": get_kpis()
    }

# ==============================================================================
# FLASK ROUTES (EXACTLY 4 CORE WEB PAGES)
# ==============================================================================

@app.route("/")
def index():
    """1. Home: Project Name, Overview, Key Metrics & Explanation."""
    df = load_data()
    countries = df.groupby("country").agg({
        "region": "first",
        "student_ai_usage_pct": "mean",
        "teacher_ai_usage_pct": "mean",
        "schools_ai_adoption_pct": "mean",
        "internet_penetration_pct": "first",
        "education_index": "first"
    }).round(2).reset_index().to_dict(orient="records")

    return render_template("index.html", countries=countries)

@app.route("/dashboard")
def dashboard():
    """2. Dashboard: The Tableau Dashboard embedding page."""
    return render_template("dashboard.html")

@app.route("/story")
def story():
    """3. Story: The Tableau Story embedding page."""
    return render_template("story.html")

@app.route("/methodology")
def methodology():
    """Methodology & Project Documentation page."""
    return render_template("methodology.html")

@app.route("/insights")
def insights():
    """4. Insights: The empirical insights achieved from the data analytics."""
    df = load_data()
    regional = df.groupby("region").agg({
        "student_ai_usage_pct": "mean",
        "teacher_ai_usage_pct": "mean",
        "schools_ai_adoption_pct": "mean",
        "internet_penetration_pct": "mean",
        "education_index": "mean",
        "gender_gap_ai_usage_pct": "mean"
    }).round(2).reset_index().to_dict(orient="records")

    policy_impact = df.groupby("government_ai_policy").agg({
        "student_ai_usage_pct": "mean",
        "teacher_ai_usage_pct": "mean",
        "schools_ai_adoption_pct": "mean"
    }).round(2).reindex(["Active", "Draft", "None"]).reset_index().to_dict(orient="records")

    curriculum_impact = df.groupby("ai_in_curriculum").agg({
        "student_ai_usage_pct": "mean",
        "teacher_ai_usage_pct": "mean",
        "schools_ai_adoption_pct": "mean"
    }).round(2).reindex(["Yes", "No"]).reset_index().to_dict(orient="records")

    return render_template(
        "insights.html",
        regional=regional,
        policy_impact=policy_impact,
        curriculum_impact=curriculum_impact
    )

@app.route("/api/summary")
def api_summary():
    """JSON summary endpoint."""
    return jsonify(get_kpis())

if __name__ == "__main__":
    print("=" * 70)
    print("GLOBAL AI ADOPTION IN EDUCATION — FLASK WEB INTEGRATION")
    print("=" * 70)
    print("Server running locally at: http://127.0.0.1:5000/")
    print(f"Tableau Dashboard URL: {TABLEAU_DASHBOARD_URL}")
    print(f"Tableau Story URL:     {TABLEAU_STORY_URL}")
    print("=" * 70)
    app.run(host="127.0.0.1", port=5000, debug=True)
