class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        q = []
        heapq.heappush(q, (0, k))

        distance = [float('inf')] * (n+1)
        distance[k] = 0

        while q:
            cost, node = heapq.heappop(q)

            if distance[node] < cost:
                continue

            for v, w in graph[node]:
                if cost + w < distance[v]:
                    temp = cost + w
                    distance[v] = temp 
                    heapq.heappush(q, (temp, v))

        answer = max(distance[1:])
        
        if answer == float('inf'):
            return -1
        
        return answer
        
