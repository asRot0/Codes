for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n-1):
        if a[i]*2 > a[i+1] and a[i+1]*2 > a[i]:
            print('yes')
            break
    else: print('no')