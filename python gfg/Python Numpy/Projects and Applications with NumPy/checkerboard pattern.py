import numpy as np

n = 8
x = np.zeros((n, n), dtype=int)
# print(x)

x[1::2, ::2] = 1
# print(x)
x[::2, 1::2] = 1
# print(x)

for i in range(n):
    for j in range(n):
        print(x[i][j], end=' ')
    print()

final = []
for i in range(n):
    final.append(np.tile([1, 0], int(n / 2)) if i & 1 else
                 np.tile([0, 1], int(n / 2)))
print(np.array(final))
