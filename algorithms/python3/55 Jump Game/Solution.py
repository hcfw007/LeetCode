class Solution:
    def canJump(self, nums):
        if (len(nums) <= 1): return True
        limit = nums[0]
        i = 0
        while (limit < len(nums) - 1 and limit > i):
            i += 1
            limit = max(limit, i + nums[i])
        return True if (limit >= len(nums) - 1) else False