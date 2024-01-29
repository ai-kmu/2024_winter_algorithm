class Solution(object):
    def arrangeCoins(self, n):
        Stairs = 0
        start = 1
        end = (n + 1) // 2
        while start <= end:
            mid = (start + end) // 2
            if (mid * (mid + 1)) // 2 <= n:
                Stairs = mid
                start = mid + 1
            else:
                end = mid - 1
        return Stairs
