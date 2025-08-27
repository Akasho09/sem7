import pandas as pd

data = {
    "Name" : ["Akash" , "Ahmad" , "Lateef"],
    "Age" : [ 10 , 20 , 30] ,
    "City" : ["Vramul" , "Sopur" , "Worpur"]
}

df = pd.DataFrame(data)

# df.to_csv("Output.csv" , index=False)
# df.to_json("Output.json")
# df.to_excel("Output.xlsx", index=False)

# n , deafukt = 5
# print(df.head())
# print(df.tail())


# 
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)

