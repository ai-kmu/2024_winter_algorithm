class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def solution(i, curr):
            if (i, curr) in memo.keys():
                return memo[(i, curr)]

            if i == len(coins) or curr > amount:
                return 0

            if curr == amount:
                return 1

            pick = solution(i, curr + coins[i])
            skip = solution(i + 1, curr)

            memo[(i, curr)] = pick + skip
            return memo[(i, curr)]

        return solution(0, 0)
