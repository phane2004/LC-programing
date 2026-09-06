class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(t), len(s)
        dp = []
        for i in range(n + 1):
            temp = []
            for j in range(m + 1):
                temp.append(0)
            dp.append(temp)
        #print(dp)

        for i in range(m + 1):
            dp[0][i] = 1
        for r in range(1, n + 1):
            for c in range(1, m + 1):
                if t[r - 1] == s[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1] + dp[r][c - 1]
                else:
                    dp[r][c] = dp[r][c - 1]
        #print(dp)
        return dp[n][m]