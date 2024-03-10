class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = [0 for _ in range(len(prices))]
        other = [0 for _ in range(len(prices))]

        hold[0] = -prices[0]

        for i in range(1, len(prices)):
            hold[i] = max(hold[i-1], other[i-2] - prices[i])
            other[i] = max(other[i-1], hold[i-1] + prices[i])

        return max(hold[-1], other[-1])
