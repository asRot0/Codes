for _ in range(int(input())):
    a, b, c = map(int, input().split())

    if (b+c) % 3 <= c:
        print(a+(b+c+2)//3)
    else:
        print(-1)


'''
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    tent = a
    if b % 3:
        gap = 3 - b % 3
        if gap <= c:
            c -= gap
            b += gap
            tent += b // 3
        else:
            print(-1)
            continue
    else:
        tent += b // 3
    tent += c // 3
    c %= 3
    tent += c // 2
    c %= 2
    tent += c
    print(tent)
'''