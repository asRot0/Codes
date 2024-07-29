import matplotlib.pyplot as plt
import numpy as np

x = (5, 5.5, 6, 6.5, 7, 8, 9, 10)
y = (120, 115, 100, 112, 80, 85, 69, 65)

plt.scatter(x, y, c='red')

z = np.polyfit(x, y, 1)
print(z)
print('---------')
p = np.poly1d(z)
print(p)
print('-----')
print(p(x))
plt.plot(x, p(x), 'c*:')
plt.show()