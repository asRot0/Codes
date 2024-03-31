for _ in range(int(input())):
    n = int(input())

    for i in range(n):
        row = ''
        for j in range(n):
            if (i+j) & 1:
                row += '..'
            else: row += '##'
        print(row)
        print(row)