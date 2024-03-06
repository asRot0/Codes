ordem = int(input())


def divisores(x):
    return [k for k in range(1, int(x / 2) + 1) if x % k == 0]


for i in range(ordem):
    entrada = int(input())
    if sum(divisores(entrada)) == entrada:
        print("%d eh perfeito" % entrada)
    else:
        print("%d nao eh perfeito" % entrada)