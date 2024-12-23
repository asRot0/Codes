for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = set(map(int, input().split()))
    q = set(map(int, input().split()))

    if k<n-1:
        print('0'*m)
        continue
    elif n==k:
        print('1'*m)
        continue
    else: print(''.join('10'[i in q] for i in a))