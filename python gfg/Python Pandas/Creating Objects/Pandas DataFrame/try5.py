import pandas as pd


# making data frame from csv file
data = pd.read_csv("../../nba.csv", index_col="Name")

print(data)
print('_'*30)

# retrieving row by loc method
d1 = data.loc["Avery Bradley"]
d2 = data.loc["R.J. Hunter"]
d3 = data.loc["Nerlens Noel"]
d4 = data.loc["Amir Johnson"]

print(d1, d2, d3, d4, sep='\n\n\n')
print('_'*30)
print(data.loc[["Nerlens Noel", "Amir Johnson"]])
print('_'*30)

print(data.head(5))

# dropping passed values
print(data.drop(["Avery Bradley", "John Holland", "R.J. Hunter"], inplace=True))
print(data.head(10))

# dropping passed columns
data.drop(["Team", "Weight", "College"], axis=1, inplace=True)
print(data.head())
