while True:
    n, m =[int(x) for x in input().split()]
    if n==m==0: break
    a = [int(x) for x in input().split()]
    t =0
    for x in range(1, n+1):
        c = a.count(x)
        if c>1: t+=1
    print(t)