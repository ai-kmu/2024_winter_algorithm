class Solution(object):
    """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
    """
    def findContentChildren(self, g, s):
        result = 0 # number of the children who have cookie
        cNum = 0
        
        g.sort() #children
        s.sort() #cookies

        for c in s: 
            if cNum == len(g):
                break
            elif c >= g[cNum]:
                result += 1
                cNum += 1

        return result