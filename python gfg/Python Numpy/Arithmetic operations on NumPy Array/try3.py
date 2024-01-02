import numpy as np

# sequence data
sequence = [2, 3, 5, 6, 7, 9]
print(sequence)

# Mean
mean = np.mean(sequence)
print('Mean -- ', mean)

# Variance
var = np.var(sequence)
print('Variance -- ', var)

# Standard Deviation
std = np.std(sequence)
print('Standard Deviation -- ', std)

# Mean Absolute Deviation
mad = np.mean(np.absolute(sequence - np.mean(sequence)))
print('Mean Absolute Deviation -- ', mad)