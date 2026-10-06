class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        li = [0] * 2051

        for start, end in logs:
            li[start] += 1
            li[end] -= 1
        #print(li[1950:2051])
        cap = 0
        res = 0
        ans = 0
        for idx in range(1950, 2051):
            cap += li[idx]
            if cap > res:
                res = cap
                ans = idx
        return ans