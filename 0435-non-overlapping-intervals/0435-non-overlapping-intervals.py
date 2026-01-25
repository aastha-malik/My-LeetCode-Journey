class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        res = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                # overlap → remove current interval
                res += 1
            else:
                # no overlap → keep it
                prev_end = intervals[i][1]
        
        return res
