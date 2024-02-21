class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while s.find(part) != -1:
            i = s.find(part)
            s = s[:i] + s[i+len(part):]
        return s


'''
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for char in s:
            stack.append(char)
            if ''.join(stack[-part_len:]) == part:
                del stack[-part_len:]
        return ''.join(stack)
'''