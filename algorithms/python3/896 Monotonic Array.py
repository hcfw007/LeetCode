class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dec = False
            if nums[i] < nums[i - 1]:
                inc = False
        return inc or dec
