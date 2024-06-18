class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        check = set('aeiou')

        for i in range(k):
            if s[i] in check: count += 1
        current = count

        for i in range(k, len(s)):
            if s[i] in check: current += 1
            if s[i-k] in check: current -= 1
            count = max(current, count)
        return count