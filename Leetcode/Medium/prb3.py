# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# sliding window

s = "abcbadab"
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global r
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            if s[r] not in seen:
                output = max(output,r-l+1)
            """
            There are two cases if s[r] in seen:
            case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            case2: s[r] is not inside the current window, we can keep increase the window
            """
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        i = 0
        res = 0

        for j in range(len(s)):
            while s[j] in check:
                check.remove(s[i])
                i += 1
            check.add(s[j])

            res = max(res, j-i+1)
        return res