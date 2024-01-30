class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            mid = (l + r) // 2
            totalCoins = self.numofCoins(mid)

            if n == totalCoins:
                return mid
            elif n < totalCoins:
                r = mid - 1
            else:
                l = mid + 1

        return r
    
    def numofCoins(self, n: int) -> int:
        # n = row
        return n * (n+1) / 2
