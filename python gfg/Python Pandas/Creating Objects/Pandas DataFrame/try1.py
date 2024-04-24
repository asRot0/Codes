import pandas as pd

li = ['hello', 'world', 'he', 'lo']

df = pd.DataFrame(li)
print(df, '\n------------')
print(df.max(), '\n----')
print(df.sum(), '\n-----')
print(df.count(), '\n--------')
print(df.to_json, '\n--------')
print(df.to_csv(), '\n---------')
print(df.to_html())
