for _ in range(int(input())):
    n = int(input())
    lov = (map(int, input().split()) for _ in range(n))
    ans = min(d + (s - 1) // 2 for d, s in lov)
    print(ans)

# -------------

for _ in range(int(input())):
    n = int(input())
    ans = min(int(x.split()[0]) + (int(x.split()[1]) - 1) // 2 for x in [input() for _ in range(n)])
    print(ans)

# -------------

for _ in range(int(input())):
    min_ans = float('inf')  # Initialize min_ans to positive infinity
    for _ in range(int(input())):
        d, s = map(int, input().split())
        min_ans = min(min_ans, d + (s-1)//2)  # Update min_ans if ans is smaller
    print(min_ans)