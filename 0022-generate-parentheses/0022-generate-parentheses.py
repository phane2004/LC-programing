class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        @cache
        def generate(o, c, s):
            if o == c == n:
                res.append(s)
                return
            if o < n:
                generate(o + 1, c, s + '(')
            if c < o:
                generate(o, c + 1, s + ')')
        generate(0, 0, "")
        return res