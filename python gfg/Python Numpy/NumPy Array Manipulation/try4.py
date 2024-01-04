# import library
import numpy as np

# Create a 2D numpy array
arr2D = np.array([[11, 11, 12, 11],
                  [13, 11, 12, 11],
                  [16, 11, 12, 11],
                  [11, 11, 12, 11]])

uniqueRows = np.unique(arr2D, axis=0)

# print the output result
print('Unique Rows:',
      uniqueRows, sep='\n')

print(np.unique(arr2D, return_index=True))
print(np.unique(arr2D, axis=1))
