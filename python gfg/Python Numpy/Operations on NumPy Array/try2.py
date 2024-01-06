# Python program showing
# Graphical representation of
# sin() function

import numpy as np
import math
import matplotlib.pyplot as plt

arr = [0, math.pi / 2, np.pi / 3, np.pi]
print('input array: ', arr)
sin_values = np.sin(arr)
print('sin values: ', sin_values)
print('- '*20)

in_array = np.linspace(-np.pi, np.pi, 12)
out_array = np.sin(in_array)
print('in_arr: ', in_array, '\nout_arr: ', out_array)

# red for numpy.sin()
plt.plot(in_array, out_array, color='red', marker='o')
plt.title('numpy.sin()')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
