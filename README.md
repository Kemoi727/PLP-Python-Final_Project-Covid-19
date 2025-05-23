COVID-19 Data Analysis Project

📁 Project Title

COVID-19 Data Analysis and Visualization

📌 Description

This project focuses on analyzing and visualizing global COVID-19 data using a dataset from Our World in Data. It provides insights into the trends of COVID-19 cases, deaths, and vaccination progress across multiple countries.

🎯 Objectives

Collect and explore a real-world COVID-19 dataset.

Clean and preprocess the data.

Perform exploratory data analysis.

Visualize trends in cases, deaths, and vaccinations.

Derive key insights and patterns.

🧰 Tools Used

Python

pandas

matplotlib

seaborn

Jupyter Notebook

📂 Dataset

Source: Our World in DataFile: owid-covid-data.csv

🚀 How to Run the Project

Clone or download the repository.

Place the owid-covid-data.csv file in your project folder.

Open the Jupyter Notebook or .py script.

Run each cell/section in order to perform the analysis.

pip install pandas matplotlib seaborn jupyter
jupyter notebook covid_analysis.ipynb

✅ Project Breakdown

1️⃣ Data Collection

Source: Our World in Data

File: owid-covid-data.csv

2️⃣ Data Loading & Exploration

Load CSV with pandas.read_csv()

Inspect columns and first few rows

Identify and count missing values

3️⃣ Data Cleaning

Filter for Kenya, India, and United States

Convert date to datetime

Drop rows with missing dates

Fill or interpolate missing values in numeric columns

4️⃣ Exploratory Data Analysis (EDA)

Line plots for total cases and total deaths over time

Compare daily new cases among countries

Calculate death rate = total_deaths / total_cases

5️⃣ Vaccination Progress Visualization

Plot cumulative vaccinations over time

Optionally include pie charts

6️⃣ (Optional) Choropleth Map

Use Plotly Express or GeoPandas

Display case/vaccine rates by country

7️⃣ Insights & Reporting

Provide 3-5 key insights from the data

Highlight trends, anomalies, and observations

📸 ERD / Data Overview

Since the project focuses on a flat CSV structure, no ERD is required. However, key columns include:

date

location

total_cases

total_deaths

new_cases

new_deaths

total_vaccinations

📊 Sample Visualizations

Total Cases Over Time

Total Deaths Over Time

New Cases Comparison

Vaccination Rollouts

📌 Notes

All plots include appropriate titles, labels, and legends.

Error handling is implemented for file loading and data type issues.

Final report includes a markdown summary of findings.
