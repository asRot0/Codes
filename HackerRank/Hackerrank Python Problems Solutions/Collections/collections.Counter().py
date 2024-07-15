x = input()
shoes = input().split()
n = input()
price = []

for i in range(int(n)):
    customer = input().split()
    if customer[0] in shoes:
        shoes.remove(customer[0])
        price.append(int(customer[1]))
        
print(sum(price))

'''
from collections import Counter
_ = input()
csize = dict(Counter(input().split()))
s = 0

for _ in range(int(input())):
    size, price = input().split()
    if (size in csize) and (csize[size] > 0) :
        csize[size] = csize[size] - 1
        s += int(price)

print(s)
'''
