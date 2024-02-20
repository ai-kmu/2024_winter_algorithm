from collections import defaultdict
import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

        graph = defaultdict(list)

        for f, t, c in flights:
            graph[f].append([t, c])
        visited = defaultdict(int)
        q = [(0, src, 0)]
        while q:

            sums, node, stopover = heapq.heappop(q)
            if node == dst:
                return sums
            if stopover > k:
                continue
            if node not in visited or visited[node] > stopover:
                visited[node] = stopover
                for t, c in graph[node]:
                    heapq.heappush(q, (sums + c, t, stopover + 1))
        return -1
