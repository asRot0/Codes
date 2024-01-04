import numpy as np
import matplotlib.pyplot as plt
import math

v = np.array((4,1))
w = v * 5
print('w = ', w)

origin = [0], [0]
plt.grid()
plt.ticklabel_format(style='sci', axis='both',
                     scilimits=(0,0))
plt.quiver(*origin, *w, scale=10)
plt.show()