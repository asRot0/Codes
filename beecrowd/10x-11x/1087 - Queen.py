while True:
    a, b, c, d = [int(i) for i in input().split(" ")]
    diferencax = abs(a - c)
    diferencay = abs(b - d)
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    else:
        if a == c and b == d:
            print(0)
        elif a == c or b == d:
            print(1)
        elif diferencax == diferencay:
            print(1)
        else:
            print(2)