class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        cnt = 0
        while (len(s) > 0 and len(g) > 0):
            s_index = s[0]
            if s[0] >= g[0]:
                cnt += 1
                s.pop(0)
                g.pop(0)
            else:
                s.pop(0)
        return cnt
