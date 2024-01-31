class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n  # 이진 탐색을 위한 초기 인덱스 설정

        while left <= right:
            mid = (left + right) // 2

            # 계단을 채우는 데 필요한 코인 수
            coins = (mid * (mid + 1)) // 2

            if coins == n:
                return mid
            elif coins < n:
                left = mid + 1
            else:
                right = mid - 1

        return right
