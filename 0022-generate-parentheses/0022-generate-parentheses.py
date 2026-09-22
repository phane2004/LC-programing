class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def helper(open, close, path):

            if open == close == n:
                res.append(path)
                return
            
            if open < n:
                helper(open + 1, close, path + '(')

            if close < open:
                helper(open, close + 1, path + ')')
        helper(0, 0, "")
        return res