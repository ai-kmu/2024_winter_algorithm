class Solution(object):
    def arrangeCoins(self, n):
        answer = int((math.sqrt(1+8*n)-1)/2)
        return answer
