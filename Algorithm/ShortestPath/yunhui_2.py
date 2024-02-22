class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append([v, w])
            
        K = 0
        visit = {}
        Q = [(0, src, 0)]
        
        while Q:
            price, node, K = heapq.heappop(Q)
            
            if node == dst:
                return price
            
            if node not in visit or visit[node] > K:
                visit[node] = K
                
                for v, w in graph[node]:
                    if K <= k:
                        alt = price + w
                        heapq.heappush(Q, (alt, v, K + 1))
                        
        return -1
