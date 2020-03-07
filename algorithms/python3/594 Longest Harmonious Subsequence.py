from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for num in count:
            if num + 1 in count:
                ans = max(ans, count[num] + count[num + 1])
        return ans
