for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = 0
    for i in range(0, n-1):
        if a[i]> b[i+1]:
            res += a[i] - b[i+1]
    print(res+a[-1])