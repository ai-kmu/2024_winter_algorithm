class Solution(object):
    """
        :type intervals: List[List[int]]
        :rtype: int
    """
    def eraseOverlapIntervals(self, intervals):
        result = -1 #output
        #끝자리 수로 정렬 후 일찍 끝나는 회의 순으로 (겹치지 않으면) ok
        #겹치면 result값 증가
        intervals.sort(key = lambda x: x[1])#배열
        crrEnd = intervals[0][1] #현재 겹쳐지지않게 배열 되는 가장 마지막 회의의 끝나는 시간
        for i in intervals:
            if i[0] >= crrEnd: #시작시간이 겹치지 않으면
                crrEnd = i[1]
            else:
                result += 1
    
        return result