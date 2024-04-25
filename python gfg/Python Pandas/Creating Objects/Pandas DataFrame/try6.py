import pandas as pd

data = pd.read_csv("../../nba.csv")
data.index += 1

print(data)
print('_' * 20)

print(data.tail())
print('_' * 20)

print(data.head(10))
print('_' * 20)

# to add a row in dataframe
# concat the old dataframe with new one

new_row = pd.DataFrame({'Name': 'Joe', 'Team': 'Boston', 'Number': 3,
                        'Position': 'PG', 'Age': 34, 'Height': '6-2',
                        'Weight': 189, 'College': 'MIT', 'Salary': 1128920},
                       index=[0])

# simply concatenate both dataframes
data = pd.concat([new_row, data]).reset_index(drop=True)
data.index += 1
print(data.head())
