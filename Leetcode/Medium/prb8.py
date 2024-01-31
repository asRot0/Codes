class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        i = res = 0
        negative = 1
        strlen = len(s)

        while i < strlen and s[i] == ' ': i += 1

        if i < strlen and s[i] == '-':
            negative, i = -1, i + 1
        elif i < strlen and s[i] == '+':
            i += 1

        while i < strlen and s[i].isdigit():
            if res > MAX_INT // 10 or (res == MAX_INT // 10 and int(s[i]) > 7):
                return MAX_INT if negative == 1 else MIN_INT
            res = res * 10 + int(s[i])
            i += 1
        return res * negative


get = Solution()
print(get.myAtoi('4193 with words'))