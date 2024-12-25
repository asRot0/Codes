for _ in range(int(input())):
    n, m = map(int, input().split())
    s = [len(input()) for i in range(n)]

    w = 0
    for i in s:
        if i>m:
            break
        else:
            w += 1
            m -= i
    print(w)