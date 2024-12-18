b = p = 0
for _ in range(int(input())):
    e, a = input().split()
    if e == 'B':
        b += int(a)
        if b > p:
            print('yes')
            b = p = 0
        else:
            p -= b
            b = 0
            print('no')
    else:
        p += int(a)
