class Solution:
    def replaceDigits(self, s: str) -> str:
        res, n = '', len(s)
        for i in range(1, n, 2):
            res += s[i-1]
            res += chr(ord(s[i-1])+int(s[i]))
        if n & 1: res += s[-1]
        return res