def minion_game(string):
    ply1, ply2 = 0, 0
    strlen = len(string)
    for i in range(strlen):
        if string[i] in 'AEIOU':
            ply1 += strlen - i
        else:
            ply2 += strlen - i
    if ply1 > ply2:
        print('Kevin', ply1)
    elif ply2 > ply1:
        print('Stuart', ply2)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
