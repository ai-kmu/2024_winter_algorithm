"""
우선순위 큐를 이용한 다익스트라 풀이 방식
- 개념 참고 링크
: https://techblog-history-younghunjo1.tistory.com/248
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # 디폴트가 list인 딕셔너리 생성
        graph = defaultdict(list)

        # 그래프 작성 - key: 출발지, value: (도착지, time)
        for u, v, w in times:
            graph[u].append((v, w))

        # 우선순위 큐 활용
        q = []
        heapq.heappush(q, (0, k))  # 시작 노드(k)에서 시작 노드로의 최단 경로는 0

        # 거리(시간) 테이블 무한대로 초기화
        distance = [float("inf")] * (n+1)
        distance[k] = 0  # 시작 노드에서 시작 노드로의 최단 경로는 0

        while q:  # 큐가 비어있지 않다면
            time, node = heapq.heappop(q)  # 최단 (시간, 노드) pop
            if time > distance[node]:  # 최단 시간(거리) 아니라면 계속 진행
                continue
            
            for v, w in graph[node]:
                if time + w < distance[v]:
                    tmp = time + w  # 갱신된 시간
                    distance[v] = tmp  # v까지 가는 최단 거리(시간) 업데이트
                    # 시작 노드에서 v까지 가는 최단 거리(시간) 우선순위 큐에 push
                    heapq.heappush(q, (tmp, v))

        dist = distance[1:]  # 노드 번호 1~n
        if max(dist) == float('inf'):  # 모든 노드에 도달하지 못한 경우
            return -1
        return max(dist)
