for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    operations = 0
    i = 0

    while i < n:
        if s[i] == 'B':
            operations += 1
            i += k
        else:
            i += 1
    print(operations)



"""
for _ in range(int(input())):
    n, k = map(int, input().split())
    s_list = list(map(str, input().strip()))
    operations = 0

    while 'B' in s_list:
        for i in range(n):
            if s_list[i] == 'B':
                j = min(i + k, n)
                for x in range(i, j):
                    s_list[x] = 'W'
                operations += 1

    print(operations)
"""
"""
t = int(input())  # Read the number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # Read n and k for the current test case
    s = input().strip()  # Read the input string and remove leading/trailing whitespaces

    operations = 0


    while 'B' in s:
        i = s.find('B')  # Find the first occurrence of 'B'
        j = s.rfind('B')  # Find the last occurrence of 'B'

        if j - i + 1 <= k:
            s = s.replace('B', 'W')
        else:
            s = s[:i] + 'W' * k + s[i + k:]

        operations += 1

    print(operations)

"""
"""
t = int(input())  # Read the number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # Read n and k for the current test case
    s = input().strip()  # Read the input string and remove leading/trailing whitespaces

    s_list = list(s)  # Convert the string to a list of characters
    operations = 0

    while 'B' in s_list:
        for i in range(n):
            if s_list[i] == 'B':
                j = min(i + k, n)  # Calculate the rightmost cell that can be changed
                for x in range(i, j):
                    s_list[x] = 'W'

                operations += 1

    print(operations)

"""
"""
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    operations = 0
    black_indices = [i for i, c in enumerate(s) if c == 'B']

    while black_indices:
        i = black_indices.pop(0)
        j = min(i + k, n)
        operations += 1

        black_indices = [idx for idx in black_indices if idx > j - 1]

    print(operations)
"""
"""
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    operation = 0

    while 'B' in s:
        i = s.find('B')
        j = min(i + k, n)
        s = s[:i] + 'W' * (j - i) + s[j:]
        operation += 1
    print(operation)

"""