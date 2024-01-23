class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        # x[1]만 해도 되는데 정렬 기준이 2개라면 이렇게 쓴다는 걸 알려주기 위해서^^
        intervals.sort(key=lambda x: (x[1], x[0]))
        last, cnt = -5 * 10**4, 0
        for interval in intervals:
            cnt += 1 if interval[0] < last else 0
            last = interval[1] if interval[0] < last else last
        return cnt
