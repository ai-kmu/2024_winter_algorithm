class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]  # [[0 (n개)],...] 2d array 0으로 초기화

        for i in range(n):  # 대각 자기자신인 경우(길이 1)
            dp[i][i] = 1


        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2 
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])     

        return dp[0][n - 1]  
            