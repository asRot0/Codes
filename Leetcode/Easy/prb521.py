class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b: return -1
        elif len(a) > len(b): return len(a)
        else: return len(b)
        # return -1 if a==b else max(lan(a), lan(b))
