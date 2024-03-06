while True:
    e = list(input().split())
    if e[0] == '*':
        break
    ans = True
    for i in e:
        if e[0][0].upper() != i[0].upper():
            ans = False
            break
    if ans:
        print('Y')
    else:
        print('N')