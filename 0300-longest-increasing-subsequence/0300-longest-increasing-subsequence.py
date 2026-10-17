class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        dp = [1] * n
        res = float('-inf')
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        #print(dp)
        return res