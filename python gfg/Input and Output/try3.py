import functools
import operator
import itertools

li = ['hello', 'world', 'me', 'letter']
print(functools.reduce(operator.add, li))

li = list(range(10))
print(li)

print(functools.reduce(lambda x, y: x + y, li))
print(functools.reduce(operator.add, li))
print(list(itertools.accumulate(li, lambda x, y: x + y)))
