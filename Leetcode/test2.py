from collections import defaultdict

n = int(input().strip())
s = input().strip()
q = int(input().strip())
results = []

for _ in range(q):
    l, r = map(int, input().strip().split())
    l -= 1
    r -= 1

    target_distinct = len(set(s[l:r+1]))

    min_length = r - l + 1
    left = l
    char_count = defaultdict(int)
    current_distinct = 0

    for right in range(l, r + 1):
        char_count[s[right]] += 1
        if char_count[s[right]] == 1:
            current_distinct += 1

        while current_distinct == target_distinct:
            min_length = min(min_length, right - left + 1)
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                current_distinct -= 1
            left += 1

    results.append(min_length)

print("\n".join(map(str, results)))
