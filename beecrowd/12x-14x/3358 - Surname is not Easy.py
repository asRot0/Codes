surname = [' eh facil', ' nao eh facil']
vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
li = []
newname = []
easy = True
ver = int(input())
for i in range(0, ver):
    name = input()
    li.append(name.capitalize())
for i in range(0, ver):
    name = len(li[i]) - 2
    for x in range(name):
        easy = True
        if li[i][x] not in vow:
            if li[i][x+1] not in vow:
                if li[i][x+2] not in vow:
                    easy = False
                    break

    if easy:
        newname.append(li[i]+surname[0])
    else:
        newname.append(li[i]+surname[1])
for i in range(0, ver):
    print(newname[i])