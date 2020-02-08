from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        count = Counter(nums)
        if k == 0:
            return sum(1 for c in count.values() if c > 1)
        return sum(1 for num in count if num + k in count)
