def print_rangoli(size):
    for i in range(size):
        s = '-'.join(chr(ord('a')+size-1-j) for j in range(i+1))
        print((s+s[::-1][1:]).center(4*size-3, '-'))
    for i in range(size -1):
        s = '-'.join(chr(ord('a')+size-1-j) for j in range(size-1-i))
        print((s+s[::-1][1:]).center(4*size-3, '-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
