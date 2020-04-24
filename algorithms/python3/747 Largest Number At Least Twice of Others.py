class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        order = sorted(range(len(nums)), key=lambda i: nums[i])
        largest, second = order[-1], order[-2]
        return largest if nums[largest] >= 2 * nums[second] else -1
