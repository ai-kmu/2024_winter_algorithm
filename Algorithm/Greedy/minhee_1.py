class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        j=0

        if len(s) == 0:
            return 0
        for i in range(len(s)):
            if j == len(g):
                break
            if s[i] >= g[j]:
                j+=1
                result+=1
        return result

        
