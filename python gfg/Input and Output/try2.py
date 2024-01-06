from functools import reduce

print('hello')
li = list(range(1, 20, 3))

li = li + list(reversed(li[:-1]))
print(li)
print(reduce(lambda x, y: x + y, li))
print(reduce(lambda x, y: x if x > y else y, li))
