for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    res = 0
    for i in range(n):
        res += (-1) ** i * a[i]
    print(res)