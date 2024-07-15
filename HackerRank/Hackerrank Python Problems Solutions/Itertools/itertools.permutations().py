from itertools import permutations

st, n = input().split()
li = list(permutations(sorted(st), int(n)))
for i in li:
    print(''.join(i))
