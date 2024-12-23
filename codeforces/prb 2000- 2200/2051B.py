for _ in range(int(input())):
    n, a, b, c = map(int, input().split())

    length = a + b + c
    cycle = n // length
    distance = cycle * length
    day = cycle * 3

    while distance < n:
        day += 1
        if day % 3 == 1:
            distance += a
        elif day % 3 == 2:
            distance += b
        else:
            distance += c
    print(day)
