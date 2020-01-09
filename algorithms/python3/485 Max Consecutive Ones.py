class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 0
        return best
