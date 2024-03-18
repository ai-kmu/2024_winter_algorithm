class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount + 1)  # 0으로 초기화
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]
        