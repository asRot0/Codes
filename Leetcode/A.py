class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        max_length = 0
        left = 0
        char_count = {}
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            while max(char_count.values()) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length


# Example usage:
sol = Solution()
print(sol.maximumLengthSubstring("bcbbbcba"))  # Output: 4
print(sol.maximumLengthSubstring("aaaa"))  # Output: 2
print(sol.maximumLengthSubstring("aaabcbbacd"))  # Output: 2


'''
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if len(s) < 3:
            return len(s)

        max_len = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub_str = s[i:j]
                char_count = {}
                duplicate_count = 0
                for c in sub_str:
                    char_count[c] = char_count.get(c, 0) + 1
                    if char_count[c] > 2: duplicate_count += 1
                if duplicate_count == 0:
                    max_len = max(max_len, len(sub_str))

        return max_len
'''