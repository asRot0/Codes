import numpy as np
import matplotlib.pyplot as plt

in_arr = [1,2,3,4]
out_arr = np.exp(in_arr)
print('in arr: ', in_arr)
print('out arr: ', out_arr)

y = [2,4,6,8]
plt.plot(in_arr, y, color='red', marker='*')

plt.plot(out_arr, y, color='blue', marker='o')

plt.title('numpy.exp()')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()