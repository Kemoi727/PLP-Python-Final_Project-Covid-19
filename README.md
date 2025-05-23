# 🦠 COVID-19 Data Analysis Project

This project is a complete data analysis pipeline for COVID-19, focusing on selected countries using a dataset from [Our World in Data](https://ourworldindata.org/coronavirus). The goal is to explore trends in cases, deaths, and vaccinations over time.

---

## 📌 Project Segments

### 1️⃣ Data Collection
- **Source:** [Our World in Data COVID-19 Dataset](https://github.com/owid/covid-19-data)
- **File Used:** `owid-covid-data.csv`
- **Format:** CSV
- **Countries Analysed:** Kenya, United States, India

---

### 2️⃣ Data Loading & Exploration
- Load CSV using `pandas`
- Inspect structure with `.head()`, `.columns`, `.info()`
- Identify missing values using `.isnull().sum()`

---

### 3️⃣ Data Cleaning
- Filtered data for Kenya, USA, and India
- Converted `date` column to datetime format
- Interpolated missing values for numeric columns:
  - `total_cases`, `total_deaths`, `new_cases`, `new_deaths`, `total_vaccinations`

---

### 4️⃣ Exploratory Data Analysis (EDA)
- **Visualizations:**
  - 📈 Line chart: Total cases and deaths over time
  - 📉 Daily new cases comparison
  - 📊 Summary statistics using `.describe()`
  - 🔢 Death rate calculation: `total_deaths / total_cases`

---

### 5️⃣ Vaccination Progress
- Analyzed and visualized cumulative vaccination trends
- Compared progress across the selected countries

---

### 6️⃣ (Optional) Choropleth Map
- Future enhancement: Create a choropleth map using Plotly or GeoPandas to show cases or vaccination rates by country.

---

### 7️⃣ Insights & Reporting
Key findings:
- 🇺🇸 The US shows significantly higher case and death counts over time.
- 🇮🇳 India experienced sharp waves of new cases.
- 🇰🇪 Kenya's vaccination progress was slower relative to others.
- 📉 A decline in new cases correlates with higher vaccination rates.

Insights are written as markdown cells in the Jupyter Notebook for easy readability.

---

## 🧰 Tools & Technologies
- Python
- Jupyter Notebook
- pandas
- matplotlib
- seaborn

---

## 📁 How to Use

1. Clone or download the repository.
2. Ensure `owid-covid-data.csv` is in the same folder.
3. Run the Jupyter Notebook:  
