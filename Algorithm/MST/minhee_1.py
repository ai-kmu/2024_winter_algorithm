class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's Algorithm
        num_node = len(points)
        q = [(0, 0)]
        visit = set()

        num_edges = 0  # 사용한 edge 수
        total_cost = 0

        while num_edges < num_node:
            cost, now_node = heapq.heappop(q)
            if now_node in visit:
                continue

            num_edges += 1
            visit.add(now_node)
            total_cost += cost

            x1, y1 = points[now_node][0], points[now_node][1]

            for node, (x2, y2) in enumerate(points):
                dist = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(q, (dist, node))

        return total_cost
