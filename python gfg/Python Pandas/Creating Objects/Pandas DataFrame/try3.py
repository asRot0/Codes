import pandas as pd

# List of nested dictionary initialization
list = [{
    "Student": [{"Exam": 90, "Grade": "a"},
                {"Exam": 99, "Grade": "b"},
                {"Exam": 97, "Grade": "c"},
                ],
    "Name": "Paras Jain"
},
    {
        "Student": [{"Exam": 89, "Grade": "a"},
                    {"Exam": 80, "Grade": "b"}
                    ],
        "Name": "Chunky Pandey"
    }
]

print(list)

# rows list initialization
rows = []

# appending rows
for data in list:
    data_row = data['Student']
    time = data['Name']

    for row in data_row:
        row['Name'] = time
        rows.append(row)

# using data frame
df = pd.DataFrame(rows)

# Increment the index so that index
# starts at 1 (0 by default)
df.index += 1

print(df)

# using pivot_table
df = df.pivot_table(index='Name', columns=['Grade'],
                    values=['Exam']).reset_index()
# Defining columns
df.columns = ['Name', 'Maths', 'Physics', 'Chemistry']

# print dataframe
print(df)
