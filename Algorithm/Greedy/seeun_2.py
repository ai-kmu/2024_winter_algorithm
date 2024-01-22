class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[1])
        num = 0
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                num += 1
                intervals[i + 1] = intervals[i]
        return num
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
