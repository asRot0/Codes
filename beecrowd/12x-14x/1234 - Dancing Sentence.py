while True:
    try:
        s = str(input())
        case = True
    except EOFError:
        break
    for i in s:
        if i == ' ':
            print(end=' ')
            continue
        if case:
            print(i.upper(), end='')
            case = False
        else:
            print(i.lower(), end='')
            case = True
    print()