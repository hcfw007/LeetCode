class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        count = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1
        degree = max(count.values())
        best = len(nums)
        for num, c in count.items():
            if c == degree:
                best = min(best, last[num] - first[num] + 1)
        return best
