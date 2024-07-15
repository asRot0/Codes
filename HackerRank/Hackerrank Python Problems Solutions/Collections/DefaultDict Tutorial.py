from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
[d[input()].append(i+1) for i in range(n)]

for _ in range(m):
    word = d[input()]
    print(*word) if word else print(-1)


'''
n, m = map(int, input().split())
d = defaultdict(lambda: -1)

for i in range(1, n + 1):
    word = input()
    d[word] = d[word] + ' ' + str(i) if word in d else str(i)
print(d)
for _ in range(m):
    print(d[input()])
 '''
