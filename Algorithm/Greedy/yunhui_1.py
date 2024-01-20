class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer = 0
        i = 0 
        j = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        while(i < len(g) and j < len(s)):
            if (g[i] <= s[j] ):   
                answer += 1
                i += 1
                j += 1
            else:
                i += 1
        
        return answer
