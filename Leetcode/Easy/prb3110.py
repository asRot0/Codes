from functools import reduce


class Solution:
    def scoreOfString(self, s: str) -> int:
        return reduce(lambda acc, i: acc + abs(ord(s[i]) - ord(s[i+1])),
                      range(len(s)-1), 0)
