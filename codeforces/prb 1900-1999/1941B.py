for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n-2):
        if a[i] > 0:
            a[i+1] -= 2 * a[i]
            a[i+2] -= a[i]
            a[i] = 0
    # print(['YES', 'NO'][any(a)])
    print(['NO', 'YES'][all(x == a[0] for x in a)])