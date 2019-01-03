class Solution:
    def jump(self, nums):
        if (len(nums) <= 1): return 0
        lastLimit = 0
        currLimit = 0
        steps = 0
        nextLimit = 0

        while (True):        
            for i in range(lastLimit, currLimit + 1):
                nextLimit = max(nextLimit, nums[i] + i)
                if (nextLimit >= len(nums) - 1): return steps + 1
            lastLimit = currLimit
            currLimit = nextLimit
            steps += 1