# Python program showing
# Graphical representation of
# tan() function

import numpy as np
import math
import matplotlib.pyplot as plt

arr = [0, math.pi / 4, 3 * np.pi / 2, math.pi / 6]
print('input array: ', arr)
tan_values = np.tan(arr)
print('tan values: ', tan_values)
print('- '*20)

in_array = np.linspace(0, np.pi, 12)
out_array = np.tan(in_array)
print('in_array: ', in_array, '\nout_array: ', out_array)

# red for numpy.tan()
plt.plot(in_array, out_array, color='red', marker='o')
plt.title('numpy.tan()')
plt.xlabel('x')
plt.ylabel('y')
plt.show()