class Solution(object):
    def removeDuplicates(self, nums):
        if (len(nums) == 0): return 0
        n = 1
        curr = nums[0]
        for i in range(1, len(nums)):
            if (nums[i] > curr):
                nums[n] = nums[i]
                curr = nums[i]
                n += 1
        return n