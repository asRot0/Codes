def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x - 1)


while True:
    try:
        a, b = [int(k) for k in input().split(" ")]
        print(fatorial(a) + fatorial(b))
    except EOFError:
        break