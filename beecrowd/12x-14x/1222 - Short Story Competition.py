from math import ceil

while True:
    try: n, l, c = map(int, input().split())
    except EOFError: break
    word = [len(i) for i in input().split()]
    char = 0
    page = 1
    for i in range(n):
        char += word[i]
        if i == len(word) - 1: break
        if char + 1 + word[i+1] > c:
            page += 1
            char = 0
        else: char += 1
    print(ceil(page / l))