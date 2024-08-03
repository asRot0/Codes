# for s in [*open(0)][1:]:a,b,c=map(int, s.split());print((abs(a-b)+2*c-1)//(2*c))

import math
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(math.ceil(abs(a-b)/(2*c)))
