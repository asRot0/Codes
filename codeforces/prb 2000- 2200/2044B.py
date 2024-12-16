seen = {'p':'q', 'q':'p', 'w':'w'}
for _ in range(int(input())):
    print(''.join(seen[c] for c in reversed(input())))