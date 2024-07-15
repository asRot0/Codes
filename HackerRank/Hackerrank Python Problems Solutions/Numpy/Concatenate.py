import numpy

n, m, p = map(int, input().split())
arr1 = numpy.array([input().split() for _ in range(n)], dtype=int)
arr2 = numpy.array([input().split() for _ in range(m)], dtype=int)
print(numpy.concatenate((arr1, arr2), axis=0))
