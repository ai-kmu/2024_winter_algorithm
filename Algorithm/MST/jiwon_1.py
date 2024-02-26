class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost = 0
        points_cnt = len(points)
        q = [(0, 0)]  # 우선순위 큐: (cost, point idx)
        visit = set()  # 방문 point 체크 set
        
        while len(visit) < points_cnt:
            cost, point_idx = heapq.heappop(q)

            # 최소 비용 연결이 되어 있다면 continue
            if point_idx in visit:
                continue
            
            visit.add(point_idx)
            min_cost += cost

            x1, y1 = points[point_idx]
            for next_idx, (x2, y2) in enumerate(points):
                # 방문하지/연결되지 않은 점에 대해서만 계산
                if next_idx not in visit:
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(q, (dist, next_idx))

        return min_cost
      
