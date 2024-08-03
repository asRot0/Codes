def is_possible(n, k, x):
    if k > x:
        return "NO"
    min_sum = (k * (k + 1)) // 2
    max_sum = (k * (2 * n - k + 1)) // 2
    if x >= min_sum and x <= max_sum:
        return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    result = is_possible(n, k, x)
    print(result)


