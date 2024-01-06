import pandas as pd

# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is',
       'portal', 'for', 'Geeks']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)

print(df)
print('_'*13)

df2 = pd.DataFrame(lst, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                   columns=['names'])
print(df2)
print('_'*13)

df3 = pd.DataFrame(zip(lst, range(1, len(2*lst), 2)),
                   index=list(chr(ord('a')+i) for i in range(len(lst))),
                   columns=['string', 'value'])
print(df3)
print('_'*13)

lst = [['tom', 25], ['krish', 30],
       ['nick', 26], ['juli', 22]]

df = pd.DataFrame(lst, columns=['Name', 'Age'])
print(df)
print('_'*13)

# list of name, degree, score
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]

# dictionary of lists
dic = {'name': nme, 'degree': deg, 'score': scr}

df = pd.DataFrame(dic)
print(df)
print('_'*13)

# data in the form of list of tuples
data = [('Peter', 18, 7),
        ('Riff', 15, 6),
        ('John', 17, 8),
        ('Michel', 18, 7),
        ('Sheli', 17, 5)]

# create DataFrame using data
df = pd.DataFrame(data, columns=['Name', 'Age', 'Score'])

print(df)
