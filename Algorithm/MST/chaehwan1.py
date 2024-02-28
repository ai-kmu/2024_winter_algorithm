class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        ad = {i:[] for i in range(size)} #관계 행렬을 딕셔너리로
        
        for i in range(size): #딕셔너리 채우기
            x1, y1 = points[i]
            
            for j in range(i+1, size):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                
                ad[i].append((dist, j))
                ad[j].append((dist, i))
                
        answer = 0
        visited = set() #방문한 노드 저장하는 곳
         #방문하지 않은점까지의 거리와 방문하지 않은점의 인덱스를 저장하는 힙큐
         #이를 (0,0)을 넣어서 초기화함(일단 0번째 index를 방문하지 않았는데 여기까지의 거리는 0이다)
        cost_idx = [(0, 0)]
        
        while len(visited) < size: # 다 돌 때까지
            minCost, neighborIdx = heappop(cost_idx)
            if neighborIdx in visited:
                continue
            
            answer += minCost
            visited.add(neighborIdx)
            
            for neighbor in ad[neighborIdx]:
                if neighbor[1] not in visited:
                    heappush(cost_idx, neighbor)
                    
        return answer
