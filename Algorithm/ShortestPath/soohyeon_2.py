class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        q = [(0, src, 0)]
        visited = [float('inf')]*n
        while q:
            count, node, stop = heapq.heappop(q)
            if node == dst:
                return count
            if stop > k:
                continue
            visited[node] = stop
            for v, w in graph[node]:
                heapq.heappush(q, (count+w, v, stop+1))
        return -1
