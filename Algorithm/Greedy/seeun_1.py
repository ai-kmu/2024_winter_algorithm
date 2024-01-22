class Solution(object):
    def findContentChildren(self, g, s):
        k_idx = 0
        c_idx = 0
        num = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        while(k_idx < len(g) and c_idx < len(s)):
            if g[k_idx] <= s[c_idx]:
                k_idx += 1
                c_idx += 1
                num += 1
            else:
                k_idx += 1
        return num
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
