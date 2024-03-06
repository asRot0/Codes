li = []
for i in range(0, 6):
    a = float(input())
    if a % 1 == 0:
        a = int(a)
    if a > 0:
        li.append(a)
print(len(li), 'valores positivos')
