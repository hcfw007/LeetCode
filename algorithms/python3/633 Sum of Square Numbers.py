class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        hi = 1
        while hi * hi <= c:
            hi += 1
        hi -= 1
        lo = 0
        while lo <= hi:
            total = lo * lo + hi * hi
            if total == c:
                return True
            elif total < c:
                lo += 1
            else:
                hi -= 1
        return False
