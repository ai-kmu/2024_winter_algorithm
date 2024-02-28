# Kruskal 알고리즘으로부터 mst_cost까지 구하는 것만 구현했습니다.
def kruskal(n, edges):
    parent = list(range(n))  # 각 노드의 부모를 자기 자신으로 초기화
    rank = [1] * n  # 각 노드의 랭크를 1로 초기화 랭크는 트리의 깊이를 나타냄.
    mst_cost = 0

    def find(x):
        # 현재 노드의 부모가 자기 자신이 아니라면 부모를 재귀적으로 찾아갑니다. 경로 압축 기법을 사용
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]  # 최종 부모를 반환

    def union(x, y):
        root_x = find(x)  # x의 루트 노드
        root_y = find(y)  # y의 루트 노드
        if root_x == root_y:
            return False
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:  # 두 루트의 랭크가 같다면
            parent[root_y] = root_x  # 한 쪽을 선택하여 다른 쪽을 자식으로 만듭니다.
            rank[root_x] += 1  # 선택된 쪽의 랭크를 증가시킵니다.
        return True  # 합침을 성공했음을 반환합니다.

    edges.sort()  # 간선을 가중치 순으로 정렬

    for u, v, weight in edges:
        if union(u, v):  # 두 노드가 다른 집합에 속해 있다면 해당 간선을 MST에 추가하고 가중치를 더함.
            mst_cost += weight
    return mst_cost
