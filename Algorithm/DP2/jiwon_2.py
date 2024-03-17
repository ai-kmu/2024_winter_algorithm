class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        len_seq = len(s)
        
        # DP 초기화: [i][j] i부터 j까지의 가장 긴 팰린드롬
        dp = [[0] * len_seq for _ in range(len_seq)]
        
        # Base case        
        for i in range(len_seq):
            dp[i][i] = 1
        
        for l in range(2, len_seq + 1):
            for i in range(len_seq - l + 1):
                j = i + l - 1
                
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][len_seq - 1]
      
