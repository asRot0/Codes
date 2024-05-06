import pandas as pd

data = pd.read_csv('../../employees.csv')

print(data.head())
print(data.columns)

data.columns = [column.replace(' ', '_') for column in data.columns]
print(data.columns)

data.query('Senior_Management == False and Gender == "Female"',
           inplace=True)
print(data.head())