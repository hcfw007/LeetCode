class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        reachable = {0}
        for num in nums:
            reachable |= {s + num for s in reachable}
            if target in reachable:
                return True
        return target in reachable
