class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        s = sum(nums) // 2
        dp = [False] * (s + 1)
        dp[0] = True
        for num in nums:
            for i in range(len(dp) - 1, num - 1, -1):
                if dp[i]:
                    continue
                if dp[i - num]:
                    dp[i] = True
                if dp[-1]:
                    return True
        return False