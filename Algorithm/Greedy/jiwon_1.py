class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)

        s_idx = 0
        answer = 0
        
        for child in g:
            if s_idx == len(s):
                break
            if s[s_idx] >= child:
                answer += 1
                s_idx += 1

        return answer
        
