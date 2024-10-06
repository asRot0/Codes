'''
for _ in range(int(input())):
    n, k = map(int, input().split())
    c = 0
    even = 0
    for i in range(n, 0,-1):
        if c == k:
            break
        c += 1
        even += i*i
    print(['yes', 'no'][even & 1])


for _ in range(int(input())):
    n, k = map(int, input().split())
    even = 0
    for i in range(n-k+1, n+1):
        even += i*i
    print(['yes', 'no'][even & 1])
'''

for _ in range(int(input())):
    n, k = map(int, input().split())

    start = n - k + 1
    odds_in_range = (n + 1) // 2 - (start // 2)

    if odds_in_range % 2 == 0:
        print("YES")
    else:
        print("NO")
