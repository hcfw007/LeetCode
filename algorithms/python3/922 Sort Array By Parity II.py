class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        even = odd = 0
        for num in nums:
            if num % 2 == 0:
                ans[even * 2] = num
                even += 1
            else:
                ans[odd * 2 + 1] = num
                odd += 1
        return ans
