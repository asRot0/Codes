while True:
    n, b = [int(x) for x in input().split()]
    if n == b == 0: break
    p = [int(x) for x in input().split()]
    a = [x for x in range(0, n+1)]
    c = list(set([abs(a-b) for a in p for b in p]))
    print('Y' if a == c else 'N')