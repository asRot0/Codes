class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        check = {}
        for word in words:
            check[word] = check.get(word, 0) + 1

        even = odd = 0
        flag = False

        for word in set(words):
            rev = word[::-1]
            if word == rev:
                if check[word] & 1:
                    even += check[word] - 1
                    flag = True
                else:
                    even += check[word]

            elif rev in check:
                odd = odd + min(check[word], check[rev])

        if flag: even += 1
        return 2 * (odd + even)

get = Solution()
print(get.longestPalindrome(["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"]))