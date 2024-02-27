class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])


        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]


        def union(a, b):
            ar = find(a)
            br = find(b)
            if ar < br:
                parent[br] = ar
            elif ar > br:
                parent[ar] = br

        edge = []
        parent = [i for i in range(len(points))]
        ans = 0
        cnt = 0

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                w = distance(points[i], points[j])
                edge.append((w, i, j))  # weight, index 1, index 2

        edge.sort()

        while edge:
            w, a, b = edge.pop(0)
            if find(a) != find(b):
                union(a, b)
                ans += w
                cnt += 1
                if cnt == len(points) - 1:
                    break

        return ans
