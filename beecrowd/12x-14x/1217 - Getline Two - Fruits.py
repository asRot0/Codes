frut = []
amt = []
kg = 0
n = int(input())

for i in range(n):
    amt.append(float(input()))
    frut = input().split()
    kg += int(len(frut))
    print('day {}: {} kg'.format(i+1, len(frut)))
    frut.clear()
print('{:.2f} kg by day'.format(kg/n))
print('R$ {:.2f} by day'.format(sum(amt)/int(len(amt))))