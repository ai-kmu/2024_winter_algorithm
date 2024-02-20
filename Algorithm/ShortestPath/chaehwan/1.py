from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, k)]

        d = defaultdict(int)

        while q:
            time, node = heapq.heappop(q)
            if node not in d:
                d[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))

        if len(d) == n:
            return max(d.values())
        return -1
