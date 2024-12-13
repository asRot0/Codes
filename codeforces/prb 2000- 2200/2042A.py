for _ in range(int(input())):
    _, k = map(int, input().split())
    for i in sorted(map(int, input().split()), reverse=True):
        if k <= i:
            print(0 if k == i else k)
            break
        k -= i
    else:
        print(k)
