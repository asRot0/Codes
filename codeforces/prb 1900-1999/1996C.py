for _ in range(int(input())):
    n, q = map(int, input().split())
    a = input()
    b = input()

    for _ in range(q):
        # Extract substrings (convert to 0-indexed)
        l, r = map(int, input().split())
        results = []
        a_sub = a[l - 1:r]
        b_sub = b[l - 1:r]

        # Count character frequencies
        a_count = [0] * 26  # For characters 'a' to 'z'
        b_count = [0] * 26  # For characters 'a' to 'z'

        for char in a_sub:
            a_count[ord(char) - ord('a')] += 1
        for char in b_sub:
            b_count[ord(char) - ord('a')] += 1

        # Calculate the minimum operations needed
        operations = 0
        for i in range(26):
            operations += abs(a_count[i] - b_count[i])

        # Since each operation can fix one excess character, we divide by 2
        results.append(operations // 2)
        print(results)


'''
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = input()
    b = input()

    for _ in range(q):
        l, r = map(int, input().split())
        a_qur = a[l - 1:r]
        b_qur = b[l - 1:r]

        a_seen = {}
        b_seen = {}

        for i, j in zip(a_qur, b_qur):
            a_seen[i] = a_seen.get(i, 0) + 1
            b_seen[j] = b_seen.get(j, 0) + 1

        opr = 0
        for char in set(a_seen.keys()).union(b_seen.keys()):
            opr += abs(a_seen.get(char, 0) - b_seen.get(char, 0))
        print(opr // 2)
'''