class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        removed, prev_end = 0, intervals[0][1]
        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                removed += 1
            else:
                prev_end = intervals[i][1]
        return removed