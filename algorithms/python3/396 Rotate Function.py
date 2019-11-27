class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        cur = sum(i * v for i, v in enumerate(nums))
        ans = cur
        n = len(nums)
        for i in range(1, n):
            cur += total - n * nums[n - i]
            ans = max(ans, cur)
        return ans
