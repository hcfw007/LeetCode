class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        total = 0
        ans = 0
        for num in nums:
            total = (total + num) % k
            ans += count.get(total, 0)
            count[total] = count.get(total, 0) + 1
        return ans
