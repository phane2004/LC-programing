class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:x[1])
        end = intervals[0][1]
        count = 0
        #print(intervals)
        for row in range(1, len(intervals)):
            if intervals[row][0] < end:
                count += 1
            else:
                end = intervals[row][1]
        return count