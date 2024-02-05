class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            li = [s[i:i+k] for i in range(0, len(s), k)]
            s = ''
            for i in li:
                s += str(sum([int(j) for j in i]))
        return s