class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self._rob_linear(nums[:-1]), self._rob_linear(nums[1:]))

    def _rob_linear(self, nums):
        prev, cur = 0, 0
        for num in nums:
            prev, cur = cur, max(cur, prev + num)
        return cur
