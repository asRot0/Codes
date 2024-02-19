def word(a):
    a = a.upper()
    for n in a:
        if not n in 'QWERTYUIOPASDFGHJKLZXCVBNM': return False
    return True
while True:
    try:
        e = str(input()).split()
    except EOFError:
        break
    s = w = 0
    for i in e:
        c =True
        if '.' in i:
            if len(i) > 1 and i.count('.') == 1 and i[-1] == '.': i = i.replace('.', '')
            else: c = False
        if not word(i): c = False
        if c:
            s += len(i)
            w += 1
    ans = int(s / w) if w != 0 else 0
    if ans <= 3: print(250)
    elif ans <= 5: print(500)
    else: print(1000)