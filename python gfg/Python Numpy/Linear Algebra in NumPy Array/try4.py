import numpy as np
import math

v = np.array([0,1,2,3,4])
print('vector -- ', v)

mgvct = math.sqrt(sum(pow(element, 2) for element in v))
print('magnitude of the vector -- ', mgvct)

# the vector using norm() method
print('magnitude of the vector -- ', np.linalg.norm(v))

vac = np.arange(3)
print('vector -- ', vac)
print('magnitude of the vector -- ', np.linalg.norm(vac))

# nth order of the magnitude of vector
print('ord is 0 -- ', np.linalg.norm(vac, ord=0))
print('ord is 1 -- ', np.linalg.norm(vac, ord=1))
print('ord is 2 -- ', np.linalg.norm(vac, ord=2))