class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            minVal = float('inf')
            while j * j <= i:
                minVal = min(minVal, dp[i - j * j] + 1)
                j += 1
            dp[i] = minVal
        return dp[-1]