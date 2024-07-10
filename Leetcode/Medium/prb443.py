from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        read = write = 0
        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1
            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write += 1
        return write


'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        count = 1

        for i in range(1, len(chars)+1):
            if i == len(chars) or chars[i] != chars[i-1]:
                chars[write] = chars[i-1]
                write += 1
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1
                count = 1
            else:
                count += 1
        del chars[write:]
        print(chars)
        return write
'''

chars = ["a","a","b","b","c","c","c"]
get = Solution()
print(get.compress(chars))