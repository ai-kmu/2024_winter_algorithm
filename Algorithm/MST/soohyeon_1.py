class Solution(object):
    def minCostConnectPoints(self, points):
        num_nodes = len(points)
        q = [(0, 0)]  # 우선순위 큐를 초기화
        visited = set()  # 방문한 노드를 추적
        num_edges = 0
        total_cost = 0
        while num_edges < num_nodes:
            cost, now_node = heapq.heappop(q)
            if now_node in visited:
                continue
            num_edges += 1
            visited.add(now_node)
            total_cost += cost
            x1, y1 = points[now_node]
            for next_node, (x2, y2) in enumerate(points):
                if next_node not in visited:
                    # 다음 노드까지의 거리를 계산하여 우선순위 큐에 추가
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(q, (dist, next_node))
        return total_cost
