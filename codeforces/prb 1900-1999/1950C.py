for _ in range(int(input())):
    h, m = map(str, input().split(':'))
    if int(h) < 12:
        if h == '00':
            print('12:'+m+' AM')
        else: print(h+':'+m+' AM')
    elif int(h) == 12:
        print('12'+':'+m+' PM')
    else:
        print(f'{int(h)-12:02d}:{m} {"PM"}')