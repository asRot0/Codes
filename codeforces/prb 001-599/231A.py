res = 0
for _ in range(int(input())):
    prb = map(int, input().strip().split())
    if sum(prb) > 1:
        res += 1
print(res)