for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    li = [0]*(n+1)
    res = ''
    for i in a:
        res += chr(ord('a')+li[i])
        li[i] += 1
    print(res)
