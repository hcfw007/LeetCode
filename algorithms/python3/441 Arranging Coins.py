class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * (mid + 1) // 2 <= n:
                lo = mid
            else:
                hi = mid - 1
        return lo
