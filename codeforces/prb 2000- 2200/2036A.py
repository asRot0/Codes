for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1):
        if abs(a[i] - a[i+1]) not in [5,7]:
            print('no')
            break
    else: print('yes')