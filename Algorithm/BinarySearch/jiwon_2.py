class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort() # 이진탐색을 위한 정렬
        cnt, len_nums = 0, len(nums)

        # 이중 for문: 삼각 부등식을 위한 두 개의 변을 선택
        for i in range(len_nums - 2):
            if nums[i] == 0:
                continue
            for j in range(i + 1, len_nums - 1):
                tmp = nums[i] + nums[j]
                left, right = j + 1, len_nums - 1

                # 삼각 부등식을 만족하는 변 탐색
                while left <= right:
                    mid = (left + right) // 2

                    if tmp <= nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                # j와 right 사이의 모든 값: 삼각 부등식을 만족
                cnt += (right - j)

        return cnt

"""
Line 12-23까지를 아래 코드로 대체 가능함
이 경우에는 from bisect import bisect_left 추가 필요

index = bisect_left(nums, tmp, j + 1)
cnt += (index - (j + 1))
"""
