import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

print(df)
print('_'*20)

# select two columns
print(df[['Name', 'Qualification']])
print('_'*20)

print(df[df.columns[1:]])
print('_'*20)


# using .loc[]
print(df.loc[0:2, ['Name', 'Age']])
print('_'*20)

print(df.loc[0, :])
print('_'*20)


# using .iloc[]
print(df.iloc[0:2, 1:3])
print('_'*20)
