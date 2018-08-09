class Solution:
    def searchRange(self, nums, target):
        first = 0
        last = len(nums) - 1

        while (first <= last):
            if (nums[first] == target and nums[last] == target):
                return [first, last]
            if (nums[first] < target):
                first += 1
            if (nums[last] > target):
                last -= 1

        return [-1, -1]