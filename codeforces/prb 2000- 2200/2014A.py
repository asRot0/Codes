for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    robin = 0
    people = 0

    for i in a:
        if i >= k:
            robin += i
        elif not i and robin:
            robin -= 1
            people += 1
    print(people)