# 인터넷에서 보고 이해한 곳 까지의 부분입니다...


class UnionFind:
    def __init__ (self, n):
        self.parents = list(range(n))
        self.weight = 0
        self.edgeCount = 0

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y, w):
        r1 = self.find(x)
        r2 = self.find(y)

        if r1 != r2:
            self.parents[r2] = r1
            self.weight += w
            self.edgeCount += 1

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        edges = [(w,a,b,i) for i, (a,b,w) in enumerate(edges)]
        edges.sort()
        uf1 = UnionFind(n)

        for w, a, b, _ in edges:
            uf1.union(a, b, w)
          
