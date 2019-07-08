class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colorCount = [0, 0, 0]
        for i in range(len(nums)): colorCount[nums[i]] += 1
        for i in range(len(nums)):
            if i < colorCount[0]:
                nums[i] = 0
            elif i < colorCount[0] + colorCount[1]:
                nums[i] = 1
            else:
                nums[i] = 2