n = list(int(num) for num in input().strip().split())[:3]
print(*sorted(n), sep="\n")
print()
print(*n, sep="\n")