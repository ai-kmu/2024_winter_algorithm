import heapq
import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        Q = [(0, k)]
        dist = {}

        while Q:
            t, node = heapq.heappop(Q)

            if node not in dist:
                dist[node] = t
                for v, w in graph[node]:
                    if v not in dist:
                        heapq.heappush(Q, (t+w, v))

        if len(dist) == n:
            return max(dist.values())
        else:
            return -1
