class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        cache = {}

        def palindrome(left, right):
            if (left, right) in cache.keys():
                return cache[(left, right)]

            if right < left:
                return 0
            if right == left:
                return 1
            
            length = 0

            if s[left] == s[right]:
                length = palindrome(left + 1, right - 1) + 2
            else:
                length += max(palindrome(left + 1, right), palindrome(left, right - 1))
            
            cache[(left, right)] = length

            return cache[(left, right)]

        return palindrome(left, right)
