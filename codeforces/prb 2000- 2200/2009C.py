import math
for _ in range(int(input())):
    x, y, k = map(int, input().split())
    if math.ceil(x/k) <= math.ceil(y/k):
        print(2 * math.ceil(y/k))
    else:
        print(2 * math.ceil(x/k)-1)