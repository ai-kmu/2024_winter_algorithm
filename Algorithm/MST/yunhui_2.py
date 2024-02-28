#미완성 코드 입니다 ㅜ.ㅜ
#UnionFind 함수까지 작성

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.n = n
    
    def union(self, a, b):
        if self.find(a) == self.find(b):
            return False
        
        self.p[self.find(a)] = self.find(b)
        self.n -= 1
        return True
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e, in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda x: x[2])

