class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        dp = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] += dp[i - 1]
            else:
                dp[i] = dp[i - 1]
        #print(dp)
        return dp[-1]