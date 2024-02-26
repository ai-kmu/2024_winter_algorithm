#wrong answer 훈수 환영 ;-D

class Solution(object):
    def kruskal(self, exI, edges, n):
        edges.sort(key = lambda x : x[2])
        visit = set()
        edgeUsed = []
        result = 0
        for i, e in enumerate(edges):
            #지정된 값 혹은 이미 양 node visit된 경우 continue
            if (i == exI) or ((e[0] in visit) and (e[1] in visit)):
                continue

            visit.update(e[:2])
            edgeUsed.append(i)
            result += e[2]
        if len(edgeUsed) < n-1:
            tmp1 = []
            for i in range(len(edges)):
                if i not in edgeUsed:
                    tmp1.append([edges[i][2],i])
            tmp = min(tmp1)
            edgeUsed.append(tmp[1])
            result += tmp[0]

        return result, edgeUsed

    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        result = [[],[]]
        mstWithAll = self.kruskal(-1,edges, n)[0]

        mst = []
        edgeuseds = set()
        for i in range(len(edges)):
            mstVal, edgeused = self.kruskal(i,edges, n)
            mst.append(mstVal)
            edgeuseds.update(edgeused)

        
        print(mstWithAll)
        for i, val in enumerate(mst):
            if val > mstWithAll:
                result[0].append(i)


        tmp = set(result[0])        
        result[1] = list(edgeuseds.difference(tmp))
        print(mst)
        return result
        
        