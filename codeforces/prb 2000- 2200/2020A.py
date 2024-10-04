for _ in range(int(input())):
    n, k = map(int, input().split())
    res = 0
    if k == 1:
        print(n)
        continue
    while n > 0:
        res += n % k
        n //= k
    print(res)
