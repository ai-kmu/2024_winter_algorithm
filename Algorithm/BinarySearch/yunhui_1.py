class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2
            coins = (mid * (mid + 1)) // 2
            
            if coins == n:
                return mid 
            
            elif coins > n:
                right = mid - 1
                
            else:
                left = mid + 1
                
        return right
