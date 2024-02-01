class Solution(object):
    def arrangeCoins(self, n):
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            coin = (mid * (mid + 1)) // 2
            if coin == n:
                return mid
            elif coin > n:
                right = mid - 1
            else:
                left = mid + 1
        return right
