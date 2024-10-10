import math
for _ in range(int(input())):
    x, y, k = map(int, input().split())
    if math.ceil(x/k) <= math.ceil(y/k):
        print(2 * math.ceil(y/k))  # y_jumps = ⌈y/k⌉ can be computed as (y + k - 1) // k
    else:
        print(2 * math.ceil(x/k)-1)  # x_jumps = ⌈x/k⌉ can be computed as (x + k - 1) // k
