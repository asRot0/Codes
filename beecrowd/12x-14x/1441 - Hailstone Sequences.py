while True:
    n = int(input())
    if n == 0:
        break
    e = [n]
    while n != 1:
        if n % 2 == 0:
            n =n//2
            e.append(n)
        else:
            n =3*n+1
            e.append(n)
    e.sort()
    print(e[-1])