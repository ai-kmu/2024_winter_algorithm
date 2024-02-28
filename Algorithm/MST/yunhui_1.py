class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_node = len(points)
        q = [(0, 0)]
        visit = set()
        
        num_edges = 0
        total_cost = 0
        
        while num_edges < num_node:
            cost, current = heapq.heappop(q)
            
            if current in visit:
                continue 
                
            num_edges += 1
            visit.add(current)
            total_cost += cost 
            
            x1, y1 = points[current][0], points[current][1]
            
            #현재 노드에서 모든 cost 계산
            for node, (x2, y2) in enumerate(points):
                dist = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(q, (dist, node))
                
        return total_cost
