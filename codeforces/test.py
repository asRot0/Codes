# Function to check if a substring of length k can be used to form s with at most one different character
def can_form_substring(s, k):
    diff_count = 0
    for i in range(0, len(s), k):
        substr = s[i:i+k]
        if len(set(substr)) > 1:
            diff_count += 1
        if diff_count > 1:
            return False
    return True

# Function to find the length of the shortest string k satisfying the conditions
def shortest_substring_length(n, s):
    for k in range(1, n + 1):
        if n % k == 0 and can_form_substring(s, k):
            return k
    return n

# Input the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    n = int(input())  # Input the length of string s
    s = input()       # Input the string s
    # Find the length of the shortest string k satisfying the conditions
    result = shortest_substring_length(n, s)
    print(result)
