# Global-Educational-Socio-Economic-Analytics-Platform
# EDA and Web Dashboard: World Education Dataset

An end-to-end data analytics project featuring an in-depth Exploratory Data Analysis (EDA) and an interactive Flask web application to visualize critical education indicators worldwide.

---

## 📌 Project Overview
This project is split into two core phases:
1. **Exploratory Data Analysis (EDA):** A detailed programmatic analysis performed in a Jupyter Notebook to clean, treat missing values, reduce data complexity, and profile global educational differences.
2. **Interactive Flask Dashboard:** A lightweight web interface built with Flask and Python that dynamically visualizes key global metrics like literacy, enrollment, completion rates, and out-of-school populations using Plotly graphs.

---

## 📊 About the Dataset
The underlying dataset features a wide-ranging view of educational metrics globally, serving as an invaluable asset for researchers, teachers, and policy makers working toward educational equity. 

### Key Features Analysed:
*   **OOSR Metrics:** Out-of-School Rates split by gender across primary and secondary education.
*   **Completion Rates:** The percentage of individuals successfully completing primary and secondary tracks.
*   **Literacy Rates:** Regional and nation-wide data emphasizing youth literacy rates (ages 15-24) broken down by gender.
*   **Socioeconomic / Demographic Factors:** Evaluation of Birth Rates, Gross Primary/Tertiary Enrollments, and country-level Unemployment Rates.

---

## 🛠️ Data Cleaning & Processing (Insights from EDA)
During the initialization phase inside the Jupyter Notebook, several data engineering adjustments were made to prepare the raw information:
*   **Placeholder Correction:** Identified that the dataset's author utilized `0` as an implicit placeholder for null elements. Standardized these by forcing a replacement map to `np.nan`.
*   **Anomaly Correction:** Erased a row containing an unidentifiable corrupted character set under index 155 (`S`).
*   **Feature Combination:** Consolidated granular sub-tracks (e.g., lower secondary vs. upper secondary metrics) into unified average benchmarks (`oosr_secondary_age_*` and `completion_rate_secondary_*`) to drop column complexity while retaining predictive strength.

---

## 📁 Repository Structure
```text
├── dataset/
│   └── global_education_data.csv  # Raw/Processed source data
├── static/
│   └── global_education_data.csv  # Active dataset for the Flask application
├── templates/
│   └── index.html                 # Main frontend template rendering Plotly charts
├── eda_notebook.ipynb             # Full data identification, cleaning, and profiling
├── app.py                         # Core Flask application script setup 
└── requirements.txt               # Required third-party software packages
