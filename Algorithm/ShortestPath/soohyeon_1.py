class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        q = []
        heapq.heappush(q, (0, k))

        distance = [float("inf")] * (n+1)
        distance[k] = 0

        while q:
            time, node = heapq.heappop(q)
            if time > distance[node]:
                continue
            for v, w in graph[node]:
                if time + w < distance[v]:
                    distance[v] = time + w
                    heapq.heappush(q, (time + w, v))
        dist = distance[1:]
        return -1 if max(dist) == float('inf') else max(dist)
