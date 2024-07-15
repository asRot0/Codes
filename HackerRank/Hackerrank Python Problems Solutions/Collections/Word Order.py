from collections import Counter
s = [input().strip() for _ in range(int(input()))]
print(len(Counter(s).keys()))
print(*Counter(s).values())
