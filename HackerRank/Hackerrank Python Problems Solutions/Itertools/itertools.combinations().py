from itertools import combinations
s, k = input().split()
for i in range(1, int(k) + 1):
    print(*[''.join(a) for a in combinations(sorted(s), i)], sep='\n')
