class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x:x[1])
        now_end = intervals[0][1]
        result =0

        for i in range(1,len(intervals)):
            if intervals[i][0] < now_end:
                result+=1
            else:
                now_end=intervals[i][1]
        return result
