class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))

        q = [(0, src, 0)]

        # 이 문제는 싸이클이 도는 그래프가 주어지기 때문에 시간초과남 - 방문 체크 필요
        # key: 노드, value: 경유 횟수
        visit = defaultdict(int)

        while q:
            cost, node, stopover = heapq.heappop(q)
            if node == dst:
                return cost

            # 방문하지 않은 경우 or 재방문의 경우에는 노드를 방문하기 이전 경유지가 더 적어야함
            # (우선순위 큐로 cost가 최소인 경로를 추출해왔기 때문)
            if node not in visit or visit[node] > stopover:
                visit[node] = stopover
                if stopover <= k:
                    for to, price in graph[node]:
                        heapq.heappush(q, (price+cost, to, stopover+1))
        
        return -1
