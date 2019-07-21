class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end, l = 0, 1, len(nums)
        if l < 2: return l
        while end <= len(nums):
            if end < len(nums) and nums[end] == nums[start]:
                end += 1
                continue
            if end - start <= 2:
                start = end
                end += 1
                continue
            del nums[start + 1:end - 1]
            start += 2
            end = start + 1
        return nums