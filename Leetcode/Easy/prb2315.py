class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        flag = True

        for c in s:
            if c == '|':
                flag = not flag
            elif flag and c == '*':
                count += 1
        return count