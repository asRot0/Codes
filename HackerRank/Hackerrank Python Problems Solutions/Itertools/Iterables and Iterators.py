from itertools import combinations

pos = 0
n = int(input())
st = input().split()
r = int(input())
li = [i+1 for i in range(n)]

ind = [i+1 for i, s in enumerate(st) if s == 'a']

com = list(combinations(li, r))

for i in com:
    if any([True for x in i if x in ind]):
        pos+=1

print('{:.4}'.format(pos/len(com)))
