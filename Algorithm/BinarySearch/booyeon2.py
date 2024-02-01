class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        result = 0

        for lstLineI in range(2,len(nums)):
            for sstLineI in range(0,lstLineI):
                rightI = lstLineI
                leftI = sstLineI
                while True:
                    mid = (leftI + rightI)//2
                    sumline = nums[sstLineI] + nums[mid]
                    if mid == leftI or mid == rightI:
                        break
                    if sumline > nums[lstLineI] :
                        rightI = mid
                    elif sumline <= nums[lstLineI]:
                        leftI = mid
                    
                result += ((lstLineI-1) - mid)

        return result
