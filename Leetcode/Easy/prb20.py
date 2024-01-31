class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in check: stack.append(i)
            elif not stack or check[stack.pop()] != i:
                return False
        return not stack
