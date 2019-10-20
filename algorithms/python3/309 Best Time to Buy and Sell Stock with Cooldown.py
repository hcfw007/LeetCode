class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = held = float('-inf')
        rest = 0
        for p in prices:
            prev_sold = sold
            sold = held + p
            held = max(held, rest - p)
            rest = max(rest, prev_sold)
        return max(sold, rest)
