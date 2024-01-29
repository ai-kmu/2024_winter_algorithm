class Solution(object):
    def triangleNumber(self, nums):
        answer = 0
        nums.sort()
        for right in range(2, len(nums)):
            left = 0
            mid = right - 1
            while left < mid:
                if nums[left] + nums[mid] > nums[right]:
                    answer += mid - left
                    mid -= 1
                else:
                    left += 1
        return answer
