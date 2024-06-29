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


'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        x=self.countAndSay(n-1)
        s=""
        y=x[0]
        ct=1
        for i in range(1,len(x)):
            if x[i]==y:
                ct+=1
            else:
                s+=str(ct)
                s+=str(y)
                y=x[i]
                ct=1
        s+=str(ct)
        s+=str(y)
        return s
'''