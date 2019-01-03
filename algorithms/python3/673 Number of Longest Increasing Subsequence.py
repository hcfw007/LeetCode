class Solution(object):
    def findNumberOfLIS(self, nums):
        n = len(nums)
        if n <= 1: return n
        lengths = [0] * n
        counts = [1] * n

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < num:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)