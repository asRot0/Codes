_, li = int(input()), set(map(int, input().split()))

for _ in range(int(input())):
    ope, *arg = input().split()
    arg_lis = list(map(int, arg))
    getattr(li, ope)(*arg_lis)
print(sum(li))
