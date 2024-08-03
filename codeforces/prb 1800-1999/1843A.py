for s in [*open(0)][2::2]:
    n = len(a:=sorted(map(int, s.split())))
    print(sum(a[n - n//2:]) - sum(a[:n//2]))