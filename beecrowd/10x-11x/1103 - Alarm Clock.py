while True:
    a, b, c, d = [int(i) for i in input().split(" ")]
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    else:
        inicial = a * 60 + b
        final = c * 60 + d
        if final <= inicial:
            final += 24 * 60
        print(final - inicial)