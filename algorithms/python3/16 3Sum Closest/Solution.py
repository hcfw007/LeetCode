class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return []
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(ans - target):
                    ans = sum
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
        return ans