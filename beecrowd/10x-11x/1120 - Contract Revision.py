while True:
    n, d = input().split()
    n, d = str(n), str(d)
    if d == n == '0':
        break
    d = d.replace(n, '')
    print(int(d)) if len(d) else print('0')
