for _ in range(int(input())):
    s = input()
    two = s.count('2')
    three = s.count('3')
    total_sum = sum(map(int, s))

    for i in range(min(two+1, 9)):
        for j in range(min(three+1, 9)):
            if (total_sum + i * 2 + j * 6) % 9 == 0:
                print('yes')
                break
        else: continue
        break
    else: print('no')