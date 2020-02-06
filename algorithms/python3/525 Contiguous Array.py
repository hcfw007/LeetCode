class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        total = 0
        ans = 0
        for i, num in enumerate(nums):
            total += 1 if num == 1 else -1
            if total in first:
                ans = max(ans, i - first[total])
            else:
                first[total] = i
        return ans
