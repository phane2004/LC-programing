class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key= lambda x:x[0])
        # print(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        res = []

        for row in range(1, len(intervals)):
            if intervals[row][0] <= end:
                if end < intervals[row][1]:
                    end = intervals[row][1]
                else:
                    continue
            else:
                res.append([start, end])
                start, end = intervals[row][0], intervals[row][1]
        res.append([start, end])
        return res