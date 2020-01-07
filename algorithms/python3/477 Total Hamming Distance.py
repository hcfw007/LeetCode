class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for bit in range(32):
            ones = 0
            for num in nums:
                ones += (num >> bit) & 1
            total += ones * (n - ones)
        return total
