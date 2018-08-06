import math

class Solution:
    def maxProfit(self, prices):
        low = math.inf
        curr_profit = 0
        prev_profit = 0
        for price in prices:
            if price > low:
                if price - low > curr_profit:
                    curr_profit = price - low
            else:
                if curr_profit > prev_profit:
                    prev_profit = curr_profit
                curr_profit = 0
                low = price
        return max(curr_profit, prev_profit)