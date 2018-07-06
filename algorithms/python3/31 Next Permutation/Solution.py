class Solution:
    def nextPermutation(self, nums):
        if (len(nums) < 2): return
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i != -1:
            j = i + 2
            while j <= len(nums) - 1:
                if nums[i] >= nums[j]:
                    break
                j += 1
            nums[i], nums[j-1] = nums[j-1], nums[i]
        m, n = i+1, len(nums)-1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1