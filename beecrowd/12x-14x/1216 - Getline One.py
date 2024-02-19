nm = []
while True:
    try:
        name = input()
        nm.append(float(input()))
    except EOFError:
        break
print('%.1f'%(sum(nm)/float(len(nm))))