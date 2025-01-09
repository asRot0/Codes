for _ in range(int(input())):
    _ = input()
    a = map(int, input().split())
    s = 0
    even = []
    for i in a:
        if not i&1:
            even.append(i)
        elif i > s:
            s = i
    even.sort()
    if s==0 or not even:
        print(0)
        continue
    cnt = len(even)
    for i in even:
        if i < s:
            s += i
        else:
            cnt += 1
            break
    print(cnt)