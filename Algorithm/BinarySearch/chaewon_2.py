import bisect

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans = 0

        while nums and nums[-1] == 0:
            nums.pop()
        nums.reverse()
    
        length = len(nums)
        if length < 3:
            return 0

        for i in range(length - 1):
            for j in range(i+1, length):
                sumOfLength = nums[i] + nums[j]
                endIndex = bisect.bisect_left(nums, sumOfLength)
                ans += endIndex - j - 1

        return ans
