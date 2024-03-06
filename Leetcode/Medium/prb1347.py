class Solution:
    def minSteps(self, s: str, t: str) -> int:
        table = {}
        count = 0

        for c in s:
            table[c] = table.get(c, 0) + 1

        for c in t:
            if c in table:
                if table[c]<1:
                    count += 1
                else: table[c] -= 1
            else: count += 1
        return count
