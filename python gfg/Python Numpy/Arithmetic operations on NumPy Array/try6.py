import numpy as np
import pandas as pd

data = [75, 69, 56, 46, 47, 79, 92, 97, 89, 88,
        36, 96, 105, 32, 116, 101, 79, 93, 91, 112]

# assume any point A
A = 79

# initialize sum to 0
s = 0

# Absolute deviation calculation
for i in data:
    av = np.absolute(i - A)

    s += av  # summing all those absolute values

# Sum divided by length of data yields
# the absolute deviation
print(s/len(data))
# print(np.mean(np.absolute(np.array(data) - A)))

# Absolute mean deviation
print(np.mean(np.absolute(data - np.mean(data))))

# Creating data frame of the given data
df = pd.DataFrame(data)

# Absolute mean deviation
print(df.mad())  # mad() is mean absolute deviation function
