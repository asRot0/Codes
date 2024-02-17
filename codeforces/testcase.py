import math

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    c = n // ((x * y) // math.gcd(x, y))
    max_elements = n // x - c
    min_elements = n // y - c
    print(((n * max_elements) - (max_elements * (max_elements - 1) // 2)) - (min_elements * (min_elements + 1) // 2))

# ------------

for _ in range(int(input())):
    _ = input()
    s = input()
    s_set = set(s)
    flag = True
    for i in s_set:
        c = s.count(i)
        if c > 1:
            indices = [j for j, char in enumerate(s) if char == i]
            if not sum(indices) & 1 == c & 1:
                flag = False
                break

    if flag:
        print('yes')
    else:
        print('no')

# -----------
