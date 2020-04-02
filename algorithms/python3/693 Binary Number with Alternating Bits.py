class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        n >>= 1
        while n:
            cur = n & 1
            if cur == prev:
                return False
            prev = cur
            n >>= 1
        return True
