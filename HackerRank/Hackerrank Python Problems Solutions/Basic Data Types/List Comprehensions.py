if __name__ == '__main__':
    x = [x for x in range(int(input()) + 1)]
    y = [x for x in range(int(input()) + 1)]
    z = [x for x in range(int(input()) + 1)]
    n = int(input())
    lis = [[i,j,k] for i in x for j in y for k in z]
    newlis = []
    for i in lis:
        if sum(i)!= n:
            newlis.append(i)
    print(newlis)
