#time out
class Solution(object):

    def cpHouse(self, index, nums):
        if index >= len(nums):
            return 0

        #강도
        robCrr = nums[index] + self.cpHouse(index + 2, nums)
        #넘어간 경우
        skipCrr = self.cpHouse(index + 1, nums)

        return max(robCrr, skipCrr)


    def rob(self, nums):
        return self.cpHouse(0, nums)