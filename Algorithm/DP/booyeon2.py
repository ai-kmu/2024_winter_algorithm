#time out
class Solution(object):

    def checkanddoState(self, index, state, prices):
        if index >= len(prices):
            return 0
        if state == 'buy':  # buy
            return max(-1 * prices[index] + self.checkanddoState(index + 1, 'sell', prices), \
                        self.checkanddoState(index + 1, 'buy', prices))
        elif state == 'sell':  # sell
            return max(prices[index] + self.checkanddoState(index + 1, 'cooldown', prices), \
                        self.checkanddoState(index + 1, 'sell', prices))
        else:  # cooldown
            return self.checkanddoState(index + 1, 'buy', prices)

    def maxProfit(self, prices):
        return self.checkanddoState(0, 'buy', prices)