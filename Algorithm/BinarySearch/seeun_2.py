def triangleNumber(nums):
    nums.sort()
    n = len(nums)
    cnt = 0
    for i in range(2, n):
        left, right = 0, i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                cnt += right - left
                right -= 1
            else:
                left += 1
    return cnt
