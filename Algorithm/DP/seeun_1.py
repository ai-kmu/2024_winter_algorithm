class Solution(object):
    def rob(self, nums):
        if len(nums) < 3:
            
            return max(nums)
     
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-3]+nums[i], dp[i-2]+nums[i])

        return dp[len(nums)-1]
