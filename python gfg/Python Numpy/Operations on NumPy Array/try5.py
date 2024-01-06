import numpy as np
import math

# degrees() function
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print("Radian values : \n", in_array)
degree_Values = np.degrees(in_array)
print("\nDegree values : \n", degree_Values)
print('- '*20)

# rad2deg() function
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print("Radian values : \n", in_array)
out_Values = np.rad2deg(in_array)
print("\nDegree values : \n", out_Values)
print('- '*20)

# degrees() function
in_array = np.arange(10.) * 90
print("Degree values : \n", in_array)
radian_Values = np.radians(in_array)
print("\nRadian values : \n", radian_Values)
print('- '*20)

# rad2deg() function
degree = np.arange(10.) * 90
print("Degree values : \n", degree)
radian = np.deg2rad(degree)
print("\nradian values : \n", radian)
