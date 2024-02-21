import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in flights:
            graph[u].append((v, w))
        
        cost = [float("inf") for _ in range(n)]
        cost[src] = 0

        heap = []
        heapq.heappush(heap, [0, src, 0])

        while heap:
            visit, node, weight = heapq.heappop(heap)
            if visit > k:
                continue
            for new_node, new_weight in graph[node]:
                if cost[new_node] > new_weight + weight:
                    cost[new_node] = new_weight + weight
                    heapq.heappush(heap, (visit + 1, new_node, new_weight + weight))

        if cost[dst] == float("inf"):
            return -1
        return cost[dst]
