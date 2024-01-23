class Solution(object):

    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        cnt = 0
        g_len = len(g)
        s_len = len(s)
        i, j = 0, 0
        while j < s_len and i < g_len:
            if g[i] <= s[j]:
                cnt += 1
                i += 1
            j += 1
        return cnt
