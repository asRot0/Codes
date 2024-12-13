for _ in range(int(input())):
    input()
    c = list(map(int, input().split()))

    freq = {}
    for i in c:
        freq[i] = freq.get(i, 0) + 1

    k = sum(v > 1 for v in freq.values())
    u = sum(v == 1 for v in freq.values())

    ceil_u_div_2 = (u + 1) // 2
    print(2 * ceil_u_div_2 + k)
