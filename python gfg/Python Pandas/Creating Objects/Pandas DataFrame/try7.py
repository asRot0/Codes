import pandas as pd

data = pd.read_csv('../../nba.csv')
print(data.head())
print('_'*20)

data.sort_values('Team', inplace=True)
condition1 = data['Team'] == 'Atlanta Hawks'

data.where(condition1, inplace=True)
print(data.head(10))
print('_'*20)

condition2 = data['Age'] > 24
data.where(condition1 & condition2, inplace=True)
print(data.head())
