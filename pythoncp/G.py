# [solved]

for _ in range(int(input())):
    over = 0
    ball = 0
    run = 0
    wic = 0
    for i in input():
        if i == 'W':
            wic += 1
            ball +=1
        else:
            run += int(i)
            ball +=1

        if ball == 6:
            over +=1
            ball =0

    overs = f"{over}.{ball} Over{'s' if over > 1 else ''}"
    runs = f"{run} Run{'s' if run > 1 else ''}"
    wickets = f"{wic} Wicket{'s' if wic > 1 else ''}"
    print(f"{overs} {runs} {wickets}.")