import pandas as pd

data = pd.read_csv("data.csv")

print(data)

data2 = pd.read_csv("https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv")

print(data2)
