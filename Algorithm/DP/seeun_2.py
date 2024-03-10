class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = [0] * n

        for i in range(1, n):      
            dp[i] = dp[i-1]    

            for j in range(i):
                if j >= 2:
                    prev_max = dp[j-2]                    
                else:
                    prev_max = 0  
                dp[i] = max(dp[i], prev_max + prices[i] - prices[j])

        return dp[-1]  
