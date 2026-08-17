class Solution:
    def helper(self, s, e, v):
        if s >= e:
            return 0
        if self.dp[s][e] != -1:
            return self.dp[s][e]
        r = 0

        for i in range(s, e+1):
            r += v[i]
        
        l = 0
        ans = 0
        for i in range(s, e):
            l += v[i]
            r -= v[i]

            if l < r: ans = max(ans, l + self.helper(s, i, v))
            elif l == r: ans = max(ans, l + max(self.helper(s, i, v), self.helper(i +1, e, v)))
            else: ans = max(ans, r + self.helper(i + 1, e, v))
        
        self.dp[s][e] = ans
        return ans
    def stoneGameV(self, stoneValue: List[int]) -> int:
        self.dp = [[-1] * 501 for _ in range(501)]
        return self.helper(0, len(stoneValue) - 1, stoneValue)