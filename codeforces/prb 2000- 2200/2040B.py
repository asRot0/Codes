for _ in range(int(input())):
    n = int(input())
    res = 2
    c = 4
    if n == 1:
        print(1)
    elif n < 5:
        print(2)
    else:
        while True:
            res += 1
            c = (c+1)*2
            if c >= n:
                break
        print(res)