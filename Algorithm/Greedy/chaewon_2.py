class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = -1
        
        start, end = intervals[0]

        for s, e in intervals:
            if s < end and e > end:
                ans += 1
            elif e <= end:
                ans += 1
                start, end = s, e
            else:
                start, end = s, e
        
        return ans
