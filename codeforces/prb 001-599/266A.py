n, s, min_stone = int(input()), input(), 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        min_stone += 1
print(min_stone)
