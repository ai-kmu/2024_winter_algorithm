class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [0]*(n+1)

        min_p = prices[0]

        for i in range(1, n+1):
            min_p = min(min_p, prices[i-1]-dp[i-2])
            dp[i] = max(dp[i-1], prices[i-1]-min_p)

        return dp[n]
