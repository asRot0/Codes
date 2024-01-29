import math

a, b = map(int, input().split())
print(int(math.log(b / a, 3 / 2) + 1))

# a, b = map(int, input().split());c=0
# while a<=b:a*=3;b*=2;c+=1
