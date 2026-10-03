class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return 0
        dp = [0] * n

        stk = []

        for i in range(n):

            if s[i] == ')' and len(stk) > 0:
                idx = stk.pop()
                dp[i], dp[idx] = 1, 1

            elif s[i] == '(':
                stk.append(i)
        # print(dp)
        res = 0
        for i in range(n):
            if i > 0  and dp[i] != 0:
                dp[i] = dp[i] + dp[i - 1]
                res = max(res, dp[i])
        return res