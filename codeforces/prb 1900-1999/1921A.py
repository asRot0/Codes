for _ in range(int(input())):
    a = [0]*4
    for i in range(4):
        a[i], _ = map(int, input().split())
    print((max(a)-min(a))**2)