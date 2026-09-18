class Solution:
    def helper(self, s, n, res):
        if n == 0:
            res.append(s)
            return

        self.helper(s + '1', n - 1, res)

        if not s or s[-1] != '0':
            self.helper(s + '0', n - 1, res)

    def validStrings(self, n: int) -> List[str]:
        res = []
        self.helper("", n, res)
        return res