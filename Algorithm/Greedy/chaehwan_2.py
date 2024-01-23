class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[1], x[0]))
        last = -5 * 10**4
        cnt = 0
        for interval in intervals:
            if interval[0] < last:
                cnt += 1
            else:
                last = interval[1]
        return cnt
