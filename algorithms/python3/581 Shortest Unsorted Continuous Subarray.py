class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        lo = 0
        while lo < len(nums) and nums[lo] == sorted_nums[lo]:
            lo += 1
        if lo == len(nums):
            return 0
        hi = len(nums) - 1
        while nums[hi] == sorted_nums[hi]:
            hi -= 1
        return hi - lo + 1
