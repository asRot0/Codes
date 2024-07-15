import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    chg_arr = numpy.array(arr, dtype=int)
    chg_arr.shape = (3,3)
    return chg_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)