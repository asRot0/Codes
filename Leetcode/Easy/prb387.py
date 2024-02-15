from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ch, val in Counter(s).items():
            if val==1:
                return s.index(ch)
        return -1


s = "leetcode"
get = Solution()
print(get.firstUniqChar(s))