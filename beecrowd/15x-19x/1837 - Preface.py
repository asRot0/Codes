a, b = map(int, input().split())
for r in range(abs(b)):
    if ((a - r) % b) == 0:
        q = (a - r) // b
        print(q, r)
        break
