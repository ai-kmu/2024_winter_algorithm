class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        end_time = intervals[0][1]
        cnt = 0
        for x in range(len(intervals) - 1):
            if intervals[x + 1][0] >= end_time:
                end_time = intervals[x+1][1]
            else:
                cnt += 1
        return cnt
