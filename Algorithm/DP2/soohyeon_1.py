class Solution(object):
    def change(self, amount, coins_list):
        dp_list = [0] * (amount + 1)
        dp_list[0] = 1
        for coin in coins_list:
            for j in range(coin, amount + 1):
                dp_list[j] = dp_list[j] + dp_list[j - coin]
        return dp_list[amount]
