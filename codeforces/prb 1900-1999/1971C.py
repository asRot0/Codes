for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a > b:
        a, b = b, a
    print(['no', 'yes'][(a<c<b) != (a<d<b)])