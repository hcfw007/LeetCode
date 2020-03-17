from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = Counter(nums)
        dup = missing = 0
        for i in range(1, n + 1):
            c = count.get(i, 0)
            if c == 2:
                dup = i
            elif c == 0:
                missing = i
        return [dup, missing]
