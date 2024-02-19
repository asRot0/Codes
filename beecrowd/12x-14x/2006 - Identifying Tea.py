while True:
    tea = int(input())
    if tea in range(1, 5):
        break
li = list(int(num) for num in input().strip().split())[0:5]
item = li.count(tea)
print(item)