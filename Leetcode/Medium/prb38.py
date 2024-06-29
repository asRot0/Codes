'''
from itertools import groupby

for i, j in groupby('12331'):
    print(list(i), list(j))
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(n, s):
            if n == 1:
                return s

            res = ''
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    res += str(count) + s[i - 1]
                    count = 1
            res += str(count) + s[-1]
            return rle(n - 1, res)

        return rle(n, '1')