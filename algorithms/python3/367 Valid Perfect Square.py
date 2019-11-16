class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        lo, hi = 1, num // 2
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
