ver = int(input())
li = []
for i in range(0, ver):
    inp = int(input())
    li.append(inp)
for i, x in enumerate(li):
    print('resposta' + ' ' + str(i+1) + ':' + ' ' + str(x))