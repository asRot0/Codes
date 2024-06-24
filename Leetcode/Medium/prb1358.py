class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        table = {'a': 0, 'b': 0, 'c': 0}
        count = 0
        left = 0
        for right in range(len(s)):
            table[s[right]] += 1

            while table['a'] > 0 and table['b'] > 0 and table['c'] > 0:
                table[s[left]] -= 1
                left += 1
            count += left
        return count