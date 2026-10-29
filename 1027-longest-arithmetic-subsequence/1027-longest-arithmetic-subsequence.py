class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        dp = [{} for _ in range(n)]
        res = 2
        for i in range(n):
            for j in range(i):
                val = nums[i] - nums[j]
                dp[i][val] = dp[j].get(val, 1) + 1
                res = max(dp[i][val], res)
        print(dp)
        return res