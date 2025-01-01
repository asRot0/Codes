for _ in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    for i in 'ABCD':
        count += min(n, s.count(i))
    print(count)