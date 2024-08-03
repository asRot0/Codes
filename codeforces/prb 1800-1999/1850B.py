for _ in range(int(input())):
    n = int(input())
    ai, bi = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        ai.append(a)
        bi.append(b)

    win = -1
    best_quality = -1
    for i in range(n):
        if ai[i] <= 10 and bi[i] > best_quality:
            win, best_quality = i+1, bi[i]
    print(win)