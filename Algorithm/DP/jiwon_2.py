class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        hold = [0] * days
        unhold = [0] * days

        hold[0] = -prices[0]
        unhold[0] = 0

        for i in range(1, days):
            hold[i] = max(unhold[i - 2] - prices[i], hold[i - 1])
            unhold[i] = max(hold[i - 1] + prices[i], unhold[i - 1])
        
        return unhold[days - 1]
