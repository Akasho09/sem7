# 7. Visualize the data
# a. Line plot of CO2 emissions over time
# b. Bar plot of average CO2 per capita
# c. Heatmap of correlation

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv")

df = pd.DataFrame(data)

df_clean = df.dropna(subset=["co2"]).copy()

# plt.figure(figsize=(10, 5))
# sns.lineplot(df_clean , x="year", y="co2", hue="country", marker="o")
# plt.title("CO₂ Emissions Over Time (2000+)")
# plt.xlabel("Year")
# plt.ylabel("CO₂ emissions (million tonnes)")
# plt.tight_layout()
# plt.show()


# b) Bar plot of average CO2 per capita (2000+)
# avg_co2pc_by_country = (
#     df_clean.groupby("country")["co2_per_capita"]
#     .mean()
#     .sort_values(ascending=False)
# )
# plt.figure(figsize=(8, 5))
# sns.barplot(
#     x=avg_co2pc_by_country.index,
#     y=avg_co2pc_by_country.values
# )
# plt.title("Average CO₂ per Capita (2000+)")
# plt.xlabel("Country")
# plt.ylabel("CO₂ per capita (tonnes)")
# plt.tight_layout()
# plt.show()



# c) Heatmap of correlation (numeric columns)
numeric_cols = ["co2", "co2_per_capita", "gdp", "population",
                "consumption_co2", "coal_co2", "oil_co2", "gas_co2"]
corr = df_clean[numeric_cols].corr(numeric_only=True)

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", square=True)
plt.title("Correlation Heatmap (2000+, selected countries)")
plt.tight_layout()
plt.show()