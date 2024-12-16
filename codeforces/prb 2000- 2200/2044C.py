for _ in range(int(input())):
    m, a, b, c = map(int, input().split())
    r1, r2 = min(m, a), min(m, b)
    print(r1+r2+min(c, 2*m-(r1+r2)))