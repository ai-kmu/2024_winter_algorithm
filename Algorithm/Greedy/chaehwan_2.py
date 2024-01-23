class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[1], x[0]))
        last, cnt = -5 * 10**4, 0
        for interval in intervals:
            cnt += 1 if interval[0] < last else 0
            last = interval[1] if interval[0] < last else last
        return cnt
