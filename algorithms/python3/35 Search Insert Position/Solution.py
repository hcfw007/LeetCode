class Solution(object):
    def searchInsert(self, nums, target):
        h = 0
        t = len(nums) - 1
        ans = 0
        while (h < t):
            c = (h + t) // 2
            if (nums[c] == target): return c
            if (nums[c] > target):
                t = c - 1
            else:
                h = c + 1
        return h + 1 if nums[h] < target else h