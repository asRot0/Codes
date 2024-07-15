from collections import deque

d = deque()
for _ in range(int(input())):
    op, *arg = input().split()
    eval(f'd.{op}({",".join(arg)})')
print(*d)

'''
from collections import deque
d = deque()
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(d, cmd)(*args)
[print(x, end=' ') for x in d]

'''
