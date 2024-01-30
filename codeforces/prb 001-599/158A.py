inp = lambda: map(int, input().strip().split())
_, k = inp()
a = list(inp())
print(sum(0 < x >= a[k - 1] for x in a))
