from itertools import combinations_with_replacement

s, r = input().split()
for i in list(combinations_with_replacement(sorted(s), int(r))):
    print(''.join(i))
