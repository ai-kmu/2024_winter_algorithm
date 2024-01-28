def binarySearch(k, lst):
    start = 0
    end = len(lst) - 1
    while end >= start and end < len(lst):
        mid = (start + end) // 2
        if lst[mid] >= k:
            end = mid - 1
        else:
            start = mid + 1
    return start


class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        while nums and nums[0] == 0:
            nums.pop(0)
        size = len(nums)
        cnt = 0
        print(nums)
        if size >= 3 and nums[0] == nums[-1]:
            return size * (size - 1) * (size - 2) / 6
        for i in range(size - 2):
            first = nums[i]
            for j in range(i + 1, size - 1):
                second = nums[j]
                cnt += binarySearch(first + second, nums[j + 1:])

        return cnt
