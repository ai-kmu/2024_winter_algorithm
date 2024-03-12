from collections import defaultdict

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = defaultdict(int)  # (i, buying) : max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if dp[(i, buying)]:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)
