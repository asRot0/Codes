t = int(input())
for _ in range(t):
    n = int(input())
    heights = []
    ropes = []

    for _ in range(n):
        a, b = map(int, input().split())
        heights.append(a)
        ropes.append(b)

    cut = 0
    for rop, hei in zip(ropes, heights):
        if rop < hei:
            cut += 1
    print(cut)