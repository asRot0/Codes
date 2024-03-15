class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for i in operations:
            count += 1 if '+' in i else -1
        return count