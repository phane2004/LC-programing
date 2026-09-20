class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        starts = sorted(x[0] for x in intervals)
        ends = sorted(x[1] for x in intervals)

        print(starts, ends)
        count = 0
        j = 0

        for i in range(len(intervals)):
            while j < len(ends) and ends[j] < starts[i]:
                #print(starts[i], ends[j])
                j += 1

            count += i - j

        return count