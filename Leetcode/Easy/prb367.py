class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        fv, lv = 1, num // 2
        while fv <= lv:
            mid = (fv+lv) // 2
            if mid**2 == num:
                return True
            else:
                if mid**2 > num:
                    lv = mid -1
                else: fv = mid +1
        return False