class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x:x[0])
        #print(intervals)
        start, end = intervals[0][0], intervals[0][1]
        res = []

        for row in range(1, len(intervals)):
            if end >= intervals[row][0]:
                if end < intervals[row][1]:
                    end = intervals[row][1]
                else:
                    continue
            else:
                res.append([start, end])
                start, end = intervals[row][0], intervals[row][1]
        res.append([start, end])
        return res
