class Solution:
    def binaryGap(self, n: int) -> int:
        best = 0
        last = None
        i = 0
        while n:
            if n & 1:
                if last is not None:
                    best = max(best, i - last)
                last = i
            n >>= 1
            i += 1
        return best
