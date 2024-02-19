while True:
    n, m = [int(x) for x in input().split()]
    if not n + m: break
    p = []
    c1 = c4 = True
    for x in range(n):
        e = [int(x) for x in input().split()]
        p.append(e)
        c = e.count(1)
        if c == len(e): c1 = False
        if c== 0: c4 = False

    p = [[x[i] for x in p]for i in range(len(p[0]))]
    c2 = c3 = True
    for x in p:
        if x.count(1) == 0: c2 = False
        if x.count(0) == 0: c3 = False
    print([c1, c2, c3, c4].count(True))