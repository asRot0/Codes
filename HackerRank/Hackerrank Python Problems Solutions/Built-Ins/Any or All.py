n, integers = int(input()), input().split()
print(all(map(lambda x: int(x)>0, integers)) and any(map(lambda x: x==x[::-1], integers)))
