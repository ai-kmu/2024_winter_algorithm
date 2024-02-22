from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # times[i] = (ui, vi, wi) ui : sourece node, vi : target node, wi : weight

        g = collections.defaultdict(list)

        for u, v, w in times:
            g[u].append((v, w))
        q = [(0, k)]

        dist = collections.defaultdict(int)

        while q:
            d, node = heapq.heappop(q)

            if node not in dist:
                dist[node] = d
                for v, w in g[node]:
                    tmp = d + w
                    heapq.heappush(q, (tmp, v))

        if len(dist) == n:
            return max(dist.values())
        else:
            return -1
