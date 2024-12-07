_ = input()
p = 0
for i in input():
    if i == '-' and p:
        p -= 1
    elif i == '+':
        p += 1
print(p)