class Solution:
    def rob(self, nums: List[int]) -> int:
        num_len = len(nums)
        
        if num_len < 3:
            return max(nums)

        dp = [0 for _ in range(num_len)]  # DP 초기화
        dp[0] = nums[0]
        dp[1] = nums[1] if nums[0] < nums[1] else nums[0]

        for i in range(2, num_len):
            now = nums[i]
            dp[i] = max(dp[i-1], dp[i-2] + now, dp[i-3] + now)

        return max(dp)
