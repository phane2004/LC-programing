class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        li = [0] * (2050 + 1)

        for start, end in logs:
            for idx in range(start, end):
                li[idx] += 1
        #print(li[1950:2051])
        res = 0
        ans = 0
        for idx in range(1950, 2051):
            if li[idx] > res:
                res = li[idx]
                ans = idx
        return ans