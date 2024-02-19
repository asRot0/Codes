class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = '0'
        for i in n:
            if i == '9': return 9
            max_digit = max(i, max_digit)
        return int(max_digit)


'''
class Solution:
    def minPartitions(self, n: str) -> int:
        for i in range(9, 0, -1):
            if str(i) in n:
                return i
'''