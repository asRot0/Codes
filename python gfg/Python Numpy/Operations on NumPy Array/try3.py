# Python program showing
# Graphical representation of
# cos() function

import numpy as np
import math
import matplotlib.pyplot as plt

arr = [0, math.pi / 2, np.pi / 3, np.pi]
print('input array: ', arr)
cos_values = np.cos(arr)
print('cos values: ', cos_values)
print('- '*20)

in_array = np.linspace(-(2*np.pi), 2*np.pi, 20)
out_array = np.cos(in_array)
print('in_array: ', in_array, '\nout_array: ', out_array)

# red for numpy.cos()
plt.plot(in_array, out_array, color='red', marker='o')
plt.title('numpy.cos()')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
