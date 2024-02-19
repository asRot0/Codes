import math
def gdc(a, b, c):
    if math.gcd(a, b, c) == 1:
        return 'tripla pitagorica primitiva'
    else:
        return 'tripla pitagorica'
while True:
    try:
        a, b, c = sorted([int(i) for i in input().split()])
    except EOFError:
        break
    if c ** 2 == a ** 2 + b ** 2:
        print(gdc(a, b, c))
    else:
        print('tripla')
