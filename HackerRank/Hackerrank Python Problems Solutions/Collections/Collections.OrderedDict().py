from collections import OrderedDict

D = OrderedDict()
for _ in range(int(input())):
    item, _, price = input().rpartition(' ')
    D[item] = D.get(item, 0) + int(price)
for item, price in D.items():
    print(item, price)
