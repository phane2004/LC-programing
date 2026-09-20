class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        s = sorted(intervals, key = lambda x:x[0])
        count = 0

        print(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                #print(val,row, s[j][0])
                if s[j][0] <= s[i][1]:
                    #print(val, s[row][j])
                    count += 1
        return count
                