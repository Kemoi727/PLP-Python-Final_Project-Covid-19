# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: Set seaborn style for cleaner plots
sns.set(style="darkgrid")

# Error Handling during File Reading
try:
    df = pd.read_csv("owid-covid-data.csv")
    print("File loaded successfully!")
except FileNotFoundError:
    print("File not found. Please check the filename and path.")
    raise
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    raise

# Data Exploration
print("\nDataset Preview:")
print(df.head())

print("\nColumns in Dataset:")
print(df.columns.tolist())

print("\nChecking for Missing Values:")
print(df.isnull().sum())

# Data Cleaning
# Filter for selected countries
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with missing dates
df = df.dropna(subset=['date'])

# Fill missing values with interpolation for smoother trends
df['total_cases'] = df['total_cases'].interpolate()
df['total_deaths'] = df['total_deaths'].interpolate()
df['new_cases'] = df['new_cases'].interpolate()
df['new_deaths'] = df['new_deaths'].interpolate()
df['total_vaccinations'] = df['total_vaccinations'].interpolate()

# Descriptive Statistics
print("\nSummary Statistics:")
print(df.describe())

# EDA Visualizations

# Total Cases Over Time
plt.figure(figsize=(12, 6))
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.tight_layout()
plt.show()

# Total Deaths Over Time
plt.figure(figsize=(12, 6))
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.tight_layout()
plt.show()

# Daily New Cases Comparison
plt.figure(figsize=(12, 6))
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['new_cases'], label=country)
plt.title('Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.tight_layout()
plt.show()

# Vaccination Over Time
plt.figure(figsize=(12, 6))
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_vaccinations'], label=country)
plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Vaccinations')
plt.legend()
plt.tight_layout()
plt.show()

# Insights
print("\n Key Insights:")
print("1. The United States shows significantly higher total cases and deaths over time.")
print("2. India had a steep rise in cases during major waves, visible in new cases trend.")
print("3. Kenya shows a slower vaccination rollout compared to the U.S. and India.")
print("4. Daily new cases vary with clear peaks corresponding to different waves.")
print("5. Vaccination progress closely correlates with a plateau in new cases in some countries.")

