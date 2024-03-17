class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]  # DP 초기화
        dp[0] = 1  # Base case
        
        for c in coins:
            for i in range(c, amount + 1):
                # 현재 금액을 만들 때 순회 중인 동전을 사용하는 경우의 수를 누적
                dp[i] += dp[i - c]
                
        return dp[amount]
