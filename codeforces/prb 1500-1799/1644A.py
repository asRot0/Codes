for _ in range(int(input())):
    seen = set()
    for i in input():
        if i in set('rgb'):
            seen.add(i)
        elif i.lower() in seen:
            seen.remove(i.lower())
        else:
            print('no')
            break
    else: print('yes')