#1번째 풀이
class Solution(object):
    def rob(self, nums):
        dp = [0 for _ in range(len(nums))]
        def f(x):
            if x>=3: dp[x] = max(dp[x-2],dp[x-3])+nums[x]
            elif x==2: dp[x] = dp[x-2]+nums[x]
            else: dp[x] = nums[x]
        

        for i in range(len(nums)):
            f(i)
        
        if len(dp) !=1:
            return max(dp[-1], dp[-2])
        else:
            return dp[0]
____________________________________________________________________
#2 두번쨰 풀이
class Solution(object):
    def rob(self, nums):
        odd, even = 0, 0
        for num in nums:
            odd, even = even, max(num + odd, even)
        return even
        
        


        

# if x>4: dp(x) = max(dp(x-2)+nums(x), dp(x-3)+nums(x))
# if x == 3: return dp(x-2) + nums(x)
# if x == 2 or 1 return nums(x)

