class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = {}
        longest = 0
        odd_char = False

        for char in s:
            table[char] = table.get(char, 0) + 1

        for count in table.values():
            if count & 1:
                longest += count - 1
                odd_char = True
            else:
                longest += count
        if odd_char: longest += 1

        return longest


get = Solution()
print(get.longestPalindrome(input()))