class Solution:
    def firstMissingPositive(self, nums):
        nums2 = [0] * (len(nums) + 2)
        for i in range(len(nums)):
            if (nums[i] >= 0 and nums[i] < len(nums) + 2):
                nums2[nums[i]] += 1
        for i in range(1, len(nums2)):
            if (nums2[i] == 0): return i
        if (len(nums) == 0): return 1
        return len(nums)