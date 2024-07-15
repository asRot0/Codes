from itertools import product
k, m = map(int, input().split())
li = (list(map(int, input().split()))[1:] for _ in range(k))
li = product(*li)
s = [sum(map(lambda x: x*x, i))%m for i in li]
print(max(s))
