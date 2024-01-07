# list comprehension

li = [x if x % 2 == 0 else x+1 for x in range(1, 20)]
print(li)

print(list(filter(lambda x: li.count(x) == 1, set(li))))
[li.remove(i) for i in filter(lambda x: li.count(x) == 1, set(li))]
print(li)
