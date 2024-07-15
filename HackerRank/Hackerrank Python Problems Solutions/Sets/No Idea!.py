_, _ = input().split()
arr = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0
for i in arr:
    if i in a:
        happiness += 1
        continue
    if i in b:
        happiness -= 1
        continue
print(happiness)
