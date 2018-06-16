class Solution(object):
    def maxSubArray(self, nums):        
        if not nums: return 0
        maximum = running_total = nums[0]
        for n in nums[1:]:
            running_total = max(running_total + n, n)
            maximum = max(running_total, maximum)
        return maximum