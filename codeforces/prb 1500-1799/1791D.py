for _ in range(int(input())):
    n = int(input())
    s = input()
    c = set()
    l = []
    for i in range(n):
        if s[i] not in c:
            c.add(s[i])
            l.append(len(set(s[:i+1])) + len(set(s[i+1:])))
    print(max(l))




'''
for _ in range(int(input())):
    n = int(input())
    s = input()
    max_sum = 0

    for i in range(1, n):
        max_sum = max(max_sum, len(set(s[:i])) + len(set(s[i:])))
    print(max_sum)
'''
