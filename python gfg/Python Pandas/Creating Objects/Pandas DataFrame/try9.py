import pandas as pd

data = pd.read_csv('../../employees.csv')
print(data.head())

# print(data.isnull())
# print(data.notnull())

bool_series = pd.isnull(data['Gender'])
print(data[bool_series].head())

bool_series = pd.notnull(data['Gender'])
print(data[bool_series].head())

# print(data.fillna(0))

data["Gender"].fillna("No Gender", inplace=True)
print(data)

new_data = data.dropna(axis=0, how='any')
print(new_data)