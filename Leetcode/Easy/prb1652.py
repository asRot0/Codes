from typing import List

'''
class Solution:
    # time complexity - O(n*k)
    # space complexity - O(n)
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        li = []
        # We extend the list by duplicating it (code * 2)
        # This allows us to handle the circular nature without complex modulo calculations
        code *= 2

        if k > 0:
            for i in range(n):
                li.append(sum(code[i + 1:i + k + 1]))

        else:
            for i in range(n):
                li.append(sum(code[i + n + k:i + n]))

        return li
'''


class Solution:
    # time complexity - O(n)
    # space complexity - O(n), auxiliary space O(1)
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n

        if k==0:
            return res

        # using sliding window
        window_sum = 0
        start_window = 1 if k > 0 else n+k
        end_window = k if k > 0 else n-1

        # initial sum
        for i in range(start_window, end_window+1):
            window_sum += code[i%n]

        for i in range(n):
            res[i] = window_sum

            window_sum -= code[start_window % n]
            window_sum += code[(end_window + 1) % n]

            start_window += 1
            end_window += 1

        return res


# code = [5, 7, 1, 4]
# k = 3
# Output: [12, 10, 16, 13]

code = [2, 4, 9, 3]
k = -2
# Output: [12, 5, 6, 13]

get = Solution()
print(get.decrypt(code, k))
