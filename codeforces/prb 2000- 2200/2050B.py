for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = sum(a) // n
    if sum(a) % n:
        print('no')

    else:
        for i in range(1, n-1):
            if a[i-1]>c:
                r = a[i-1] - c
                a[i-1] -= r
                a[i+1] += r
            elif a[i-1]<c:
                r = c - a[i-1]
                a[i-1] += r
                a[i+1] -= r
        print(['no','yes'][len(set(a))==1])


'''
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c, s = divmod(sum(a), n)
    if s:
        print('no')
        continue
    for i in range(1, n-1):
        r = a[i-1] - c
        a[i-1] -= r
        a[i+1] += r
    print('yes' if len(set(a)) == 1 else 'no')

'''