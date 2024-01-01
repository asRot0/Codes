n = 5
result = []

for i in range(n):
    row = [n - j if j <= i else n - i for j in range(n)]
    row += row[-2::-1]
    result.append(row)

for i in result:
    print(' '.join(map(str, i)))
for i in result[-2::-1]:
    print(' '.join(map(str, i)))

# ---------------

n = int(input())
result = [[n - j if j <= i else n - i for j in range(n)] +
          [n - i if j > i else n - j for j in range(n - 2, -1, -1)]
          for i in range(n)]

for r in result:
    print(*r)
for r in result[-2::-1]:
    print(*r)

"""
7 7 7 7 7 7 7 7 7 7 7 7 7
7 6 6 6 6 6 6 6 6 6 6 6 7
7 6 5 5 5 5 5 5 5 5 5 6 7
7 6 5 4 4 4 4 4 4 4 5 6 7
7 6 5 4 3 3 3 3 3 4 5 6 7
7 6 5 4 3 2 2 2 3 4 5 6 7
7 6 5 4 3 2 1 2 3 4 5 6 7
7 6 5 4 3 2 2 2 3 4 5 6 7
7 6 5 4 3 3 3 3 3 4 5 6 7
7 6 5 4 4 4 4 4 4 4 5 6 7
7 6 5 5 5 5 5 5 5 5 5 6 7
7 6 6 6 6 6 6 6 6 6 6 6 7
7 7 7 7 7 7 7 7 7 7 7 7 7
"""
