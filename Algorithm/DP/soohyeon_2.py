class Solution:
    infinite = float('inf')

    def maxProfit(self, prices):
        buying_price = self.infinite
        free, last_profit, current_profit = 0, 0, 0
        for price in prices:
            current_profit = max(last_profit, price - buying_price)
            buying_price = min(buying_price, price - free)
            free, last_profit = last_profit, current_profit

        return current_profit
