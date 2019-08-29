class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result
