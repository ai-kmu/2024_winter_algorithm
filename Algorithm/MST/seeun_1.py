from heapq import heappop, heappush


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        q = [(0, points[0][0], points[0][1])]
        total = 0

        while q:
            dis, x, y = heappop(q)
            if (x, y) in visited:
                continue

            total += dis
            visited.add((x, y))

            for i in range(len(points)):
                a, b = points[i]
                if (a, b) not in visited:
                    dist = abs(x - a) + abs(y - b)
                    heappush(q, (dist, a, b))

        return total
