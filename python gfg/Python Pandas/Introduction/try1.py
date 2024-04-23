import pandas as pd
import numpy as np

ser = pd.Series()
print("Pandas empty Series: ", ser)

data = np.array(['h', 'e', 'k'])

ser = pd.Series(data)
print("Pandas Series:", ser, sep='\n')
