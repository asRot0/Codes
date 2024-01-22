import math
for _ in range(int(input())):
    _ = input()
    a = math.sqrt(sum(map(int, input().split())))
    print('YES' if a == int(a) else 'NO')