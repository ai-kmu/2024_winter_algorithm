from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        g = collections.defaultdict(list)

        for fromi, toi, pricei in flights:
            g[fromi].append([toi, pricei])

        visit = {}

        q = [(0, src, 0)]  # price,src,k

        while q:
            p, N, K = heapq.heappop(q)
            if N == dst:
                return p
            if N not in visit or visit[N] > K:
                visit[N] = K
                for toi, pricei in g[N]:
                    if K <= k:
                        tmp = p + pricei
                        heapq.heappush(q, [tmp, toi, K+1])

        return -1
