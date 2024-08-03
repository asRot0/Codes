n = int(input())
events = list(map(int, input().split()))

free_policemen = 0
untreated_crimes = 0

for event in events:
    if event == -1:
        if free_policemen > 0:
            free_policemen -= 1
        else:
            untreated_crimes += 1
    else:
        free_policemen += event
print(untreated_crimes)