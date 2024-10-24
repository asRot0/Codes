for _ in range(int(input())):
    n, k = map(int, input().split())
    li = []
    res = []
    for _ in range(n):
        li.append(input())

    a = n // k
    for i in range(0, n, k):
        for j in li[i][::k]:
            res.append(j)
    # print(res)
    # print(''.join(res))
    for i in range(0, len(res), a):
        print(''.join(res[i:i+a]))