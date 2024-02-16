import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))  # node, cost
        
        cost = [float("inf") for _ in range(n+1)]
        cost[k] = 0

        heap = []
        heapq.heappush(heap, [0, k])

        while heap:
            c, node = heapq.heappop(heap)
            if cost[node] < c:
                continue
            for neighbor, new_cost in graph[node]:
                if cost[neighbor] > c + new_cost:
                    cost[neighbor] = c + new_cost
                    heapq.heappush(heap, [cost[neighbor], neighbor])

        ans = max(cost[1:])
        if ans == float("inf"):
            return -1
        else:
            return ans
