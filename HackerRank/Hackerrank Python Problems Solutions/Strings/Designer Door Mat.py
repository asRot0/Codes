n, m = list(map(int, input().split()))
for i in range(1, int((n+1)/2)):
    print(('.|.'*(2*i - 1)).center(m, '-'))
print('WELCOME'.center(m, '-'))
for i in range(int((n-1)/2), 0, -1):
    print(('.|.'*(2*i - 1)).center(m, '-'))
