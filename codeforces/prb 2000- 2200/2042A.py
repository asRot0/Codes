for _ in range(int(input())):
    _, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in a:
        if k==i:
            print(0)
            break
        elif k<i:
            print(k)
            break
        else: k -= i
    else: print(k)