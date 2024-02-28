class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # prim's Algorithm
        def prim(edges, tmp_edge=None):

            # 그래프 추가
            edge_list = [[] for _ in range(n)]

            for i, (u, v, w) in enumerate(edges):
                # 양방향 그래프이므로
                edge_list[u].append((v, w, i))
                edge_list[v].append((u, w, i))

            visit = [0] * n
            total_w = 0
            q = []

            # edges[tmp_edge]를 넣어놓고 시작
            if tmp_edge is not None:
                input_u, input_v, input_w = edges[tmp_edge]
                visit[input_u] = 1
                visit[input_v] = 1
                total_w += input_w

                for v, w, i in edge_list[input_u]:
                    heapq.heappush(q, (w, v, i))
                for u, w, i in edge_list[input_v]:
                    heapq.heappush(q, (w, u, i))

            else:
                heapq.heappush(q, (0, 0, -1))

            while q:
                w, v, i = heapq.heappop(q)
                if visit[v] == 0:
                    visit[v] = 1
                    total_w += w
                    # v에서 출발 할수 있는 edge들을 q에 추가
                    for v_u, v_w, v_idx in edge_list[v]:
                        if visit[v_u] == 0:
                            heapq.heappush(q, (v_w, v_u, v_idx))

            if sum(visit) != n:
                return float("inf")

            return total_w

        mst_w = prim(edges)  # MST answer

        critical = []
        pseudo_critial = []

        # critical 확인 (i번째 edge 빼고 MST돌림)
        for i in range(len(edges)):
            tmp_w = prim(edges[:i]+edges[i+1:])
            if tmp_w > mst_w:
                critical.append(i)

        # pseudo_critial 확인 (i번째 edge를 먼저 넣어놓고 MST돌림)
        for i in range(len(edges)):
            if i not in critical:
                tmp_w = prim(edges, i)
                print(tmp_w)
                if tmp_w == mst_w:
                    pseudo_critial.append(i)

        return [critical, pseudo_critial]
