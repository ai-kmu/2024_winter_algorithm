class Solution:   
    def __init__(self):
        self.parent = []


    def findParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]


    def unionParent(self, a, b):
        a = self.findParent(a)
        b = self.findParent(b)
        if a < b:
            self.parent[b] = a
        else:
            self.parent[a] = b


    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # kruskal 사용을 위한 edge 리스트 생성 및 오름차순 정렬
        sorted_edges = []
        for idx, (a, b, w) in enumerate(edges):
            sorted_edges.append([idx, a, b, w])

        sorted_edges = sorted(sorted_edges, key=lambda x: x[3])
        print(sorted_edges)
        
        self.parent = [i for i in range(n)]  # 0부터 n-1까지 부모 테이블 초기화

        mst_edges = []
        mst_cost = 0

        # kruskal's algorithm
        for idx, a, b, w in sorted_edges:
            # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은 것
            if self.findParent(a) != self.findParent(b):
                self.unionParent(a, b)
                mst_cost += w
                mst_edges.append(idx)


        return 0
