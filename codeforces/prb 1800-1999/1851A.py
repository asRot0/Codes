def find_possible_steps(hi, m, k, H):
    possible_steps = set()
    for j in range(m):
        step_height = j * k
        if (H + step_height - hi) % k == 0:
            possible_step = 1 + (H + step_height - hi) // k
            if 1 <= possible_step <= m and possible_step != j + 1:
                possible_steps.add(possible_step)
    return possible_steps

def vlad_conversation(t, test_cases):
    results = []
    for i in range(t):
        n, m, k, H = test_cases[i][0]
        heights = test_cases[i][1]

        conversation_count = 0
        for hi in heights:
            possible_steps = find_possible_steps(hi, m, k, H)
            if possible_steps:
                conversation_count += 1

        results.append(conversation_count)

    return results

# Input the number of test cases
t = int(input())

# Process each test case
test_cases = []
for _ in range(t):
    n, m, k, H = map(int, input().split())
    heights = list(map(int, input().split()))
    test_cases.append(((n, m, k, H), heights))

results = vlad_conversation(t, test_cases)

# Output the results
for result in results:
    print(result)
