_, st = input(), set(map(int, input().split()))
for _ in range(int(input())):
    op, _ = input().split()
    arg = set(map(int, input().split()))

    exec('st.' + op + '(' + str(arg) + ')')
print(sum(st))
