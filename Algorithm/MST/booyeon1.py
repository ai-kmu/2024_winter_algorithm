#time_out 69/72

class Solution(object):
    def manhDisWithAll(self, point, unvisit):
        result = [float('inf'),0]  #[weight, min_index(at unvisit)]
        for i in range(len(unvisit)):
            manhDis = abs(point[0]-unvisit[i][0]) \
                            + abs(point[1]-unvisit[i][1])
            if manhDis < result[0]:
                result = [manhDis, i]

        return result

    def minCostConnectPoints(self, points):
        unvisit = points
        visit = [unvisit.pop(0)]
        result = 0

        for i in range(len(unvisit)):
            minNodes = []
            for edgePoint in visit:
                minNodes.append(self.manhDisWithAll(edgePoint,unvisit))
            minNode = min(minNodes)
            visit.append(unvisit.pop(minNode[1]))
            result += minNode[0]
        

        return result