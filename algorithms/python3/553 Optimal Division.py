class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return "{}/{}".format(nums[0], nums[1])
        return "{}/({})".format(nums[0], "/".join(str(n) for n in nums[1:]))
