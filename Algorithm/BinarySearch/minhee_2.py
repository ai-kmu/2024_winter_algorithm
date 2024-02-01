class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        result =0

        if len(nums) < 3: 
            return result
        
        for r in range(len(nums)-1,1,-1):
            l = 0
            m = r-1
            while l < m:
                if nums[l]+nums[m] > nums[r]:
                    result += m-l
                    m -= 1
                else:
                    l += 1
        return result     
