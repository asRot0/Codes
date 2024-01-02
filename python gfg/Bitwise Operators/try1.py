a, b = 10, 4
print(a | b)
print(a & b)
print(id(a), id(b), sep='\n')
a = a >> 1
b = b << 1
print(a)
print(id(a))
a += b
print(a)
print(id(a))
