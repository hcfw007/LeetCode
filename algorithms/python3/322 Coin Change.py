class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for a in range(coin, amount + 1):
                if dp[a - coin] + 1 < dp[a]:
                    dp[a] = dp[a - coin] + 1
        return dp[amount] if dp[amount] != float('inf') else -1
