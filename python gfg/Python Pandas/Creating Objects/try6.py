import pandas as pd

data = pd.read_csv("../nba.csv", index_col="Name")
first = data["Age"]
print(first)
print('_'*20)

first = data.loc["Avery Bradley"]
print(first)
print('_'*20)

row = data.iloc[3]
print(row)