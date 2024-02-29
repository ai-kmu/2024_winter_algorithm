class UnionFind:

    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
    

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

            
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]      
        return x
        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        n_edges = len(edges)
        n_nodes = n

        uf = UnionFind(n_nodes)

        critical = []
        pseudo = set()

        def tarjan(cur_node, parent_edge):
            id = len(dfn)
            low[cur_node] = id
            dfn[cur_node] = id

            neighbors = graph[cur_node]

            for comp_id, edge_id in neighbors:
                if edge_id == parent_edge:
                    continue
                if comp_id not in dfn:
                    tarjan(comp_id, edge_id)
                    low[cur_node] = min(low[cur_node], low[comp_id])
                    if low[comp_id] > dfn[cur_node]:
                        critical.append(edge_id)
                        pseudo.discard(edge_id)
                else:
                    low[cur_node] = min(dfn[comp_id], low[cur_node])



        # edges排序
        sorted_edges = []
        for i, (u, v, w) in enumerate(edges):
            edge = (w, u, v, i)
            sorted_edges.append(edge)
        sorted_edges.sort()

        
        start = 0
        while start < n_edges:
            end = start
            #weight같은 것들끼리 묶기
            while end < n_edges and sorted_edges[end][0] == sorted_edges[start][0]:
                end += 1

            comp_map = {} # node_idx -> comp_id
            comp_id = 0
            for _, node1, node2, _ in sorted_edges[start: end]:
                root1 = uf.find(node1)
                root2 = uf.find(node2)
                if root1 != root2:
                    if root1 not in comp_map:
                        comp_map[root1] = comp_id
                        comp_id += 1
                    if root2 not in comp_map:
                        comp_map[root2] = comp_id
                        comp_id += 1
            
            graph = collections.defaultdict(list)
            # graph = {} # comp_id -> [(comp_id, edge_id) , ...]

            for _, node1, node2, edge_id in sorted_edges[start: end]:
                root1 = uf.find(node1)
                root2 = uf.find(node2)
                if root1 != root2:
                    comp1_id = comp_map[root1]
                    comp2_id = comp_map[root2]
                    
                    graph[comp1_id].append((comp2_id, edge_id))
                    graph[comp2_id].append((comp1_id, edge_id))
                    pseudo.add(edge_id)
            
            low = {}
            dfn = {}
            for comp in range(comp_id):
                if comp not in dfn:
                    tarjan(comp, -1)
            
            for _, node1, node2, _ in sorted_edges[start: end]:
                uf.union(node1, node2)
            
            start = end
        
        return [critical, list(pseudo)]
