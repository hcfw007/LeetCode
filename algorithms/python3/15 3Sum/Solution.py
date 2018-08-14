class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if (i > 0 and nums[i-1] == nums[i]): continue
            l, r = i + 1, len(nums) - 1
            while (l < r):
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1; r -= 1
                    while (l < r) and nums[l] == nums[l-1]: l += 1
                    while (l < r) and nums[r] == nums[r+1] : r -= 1
                elif s < 0:
                    l += 1
                else:
                   r -= 1
        return ans