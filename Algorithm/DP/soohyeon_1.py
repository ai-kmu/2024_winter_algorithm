class Solution:
    def rob(self, nums):
        prev_max = 0
        curr_max = 0
        
        for amount in nums:
            new_max = max(amount + prev_max, curr_max)
            prev_max, curr_max = curr_max, new_max
        
        return curr_max