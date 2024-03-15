class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr == substr[::-1]:
                    if len(substr) > len(longest):
                        longest = substr
            remaining = s[i:]
            if remaining == remaining[::-1]:
                if len(remaining) >= len(longest):
                    return remaining
        return longest
