class Solution(object):
    def change(self, amount, coins):
        # dp[i][j]: coins[0]부터 coins[i]까지 사용해서 j금액을 만들 수 있는 경우의 수
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        
        # 0원을 만드는 경우의 수는 항상 1이므로 초기화
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                # 현재 동전을 사용하지 않는 경우와 사용하는 경우를 더해줌
                dp[i][j] = dp[i - 1][j] + (dp[i][j - coins[i - 1]] if j >= coins[i - 1] else 0)

        return dp[len(coins)][amount]
