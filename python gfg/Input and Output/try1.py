num_list = list(range(15))

even_double = map(lambda x: x * 2 if x % 2 == 0 else x, num_list)
print(list(even_double))
