class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = prev1 = 0
        for c in cost:
            prev2, prev1 = prev1, min(prev1, prev2) + c
        return min(prev1, prev2)
