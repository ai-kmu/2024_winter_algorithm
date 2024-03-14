class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
         
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for idx in range(coin, amount + 1):
                if coin <= idx:
                    dp[idx] += dp[idx-coin]

        return dp[amount]
