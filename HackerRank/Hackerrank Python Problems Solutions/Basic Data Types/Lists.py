li = []
n = int(input())
for _ in range(n):
    ope, *arg = input().split()
    arg_lis = list(map(int, arg))
    if ope == 'print':
        print(li)
    else:
        getattr(li, ope)(*arg_lis)
