import numpy as np
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv")

df = pd.DataFrame(data)

# 4. Explore the Data
# a. First 5 rows of the dataset
# b. Print the head of the data
# c. Print summary statistics

# print(data.head())
# print(data.tail(10))
# print("\nSummary statistics:")
# print(df.describe())

# 3. Filter the dataset for a manageable subset, years 2000 onward and 
# selected countries, 'India', 'United States', 'China', 'Germany', 'Brazil'

# countries = ['India', 'United States', 'China', 'Germany', 'Brazil']
# df = df[(df['year']>2020) & (df["country"].isin(countries))]

# print(df.head(10))


# 5. Clean the data
# a. Check for missing values in key columns
# b. Drop rows with missing CO2 data

# print("Missing values before cleaning:")
# print(df[["country", "year", "cement_co2", "population", "gdp"]].isnull().sum())
# print(f"\nDataset shape before cleaning: {df.shape}")


# # b. Drop rows with missing CO2 data
# df = df.dropna(subset=["cement_co2"])
# print("\nMissing values after dropping rows with missing CO2:")
# print(df[["country", "year", "cement_co2", "population", "gdp"]].isnull().sum())

# print(f"\nDataset shape after cleaning: {df.shape}")

# 6. Data Mining and Analysis
# a. Compute Mean CO2 emissions per country
# b. Compute maximum CO2 emissions per year

mean_co2_per_country = df.groupby("country")["co2"].mean().reset_index()
mean_co2_per_country.columns = ["country", "mean_co2"]
print("Mean CO2 emissions per country (2000 onward):")
print(mean_co2_per_country)

maxEmm = df.groupby("year")["co2"].max().reset_index()
maxEmm.columns = ["Year" , "Max CO2"]
print("\nMaximum CO2 emissions per year:")
print(maxEmm)


