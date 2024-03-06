while True:
    n = input()
    if '-' in n:
        break
    if '0x' in n:
        print(int(n, 16))
    else:
        h = hex(int(n))
        print(h[:2] + h[2:].upper())