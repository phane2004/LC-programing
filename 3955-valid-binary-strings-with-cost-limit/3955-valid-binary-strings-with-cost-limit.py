class Solution:
    def cost(self, s):
        cst = 0
        # print(s)
        for idx, val in enumerate(s):
            # print(val, idx)
            if val == "1":
                cst += idx
        return cst

    def helper(self, s, k, res, n):
        if (len(s) > 1 and s[-1] == "1" and s[-1] == s[-2]) or self.cost(s) > k:
            return
        s = s
        if len(s) == n:
            res.append(s)
            # print(res, self.cost(s), end =  "")
            # print()
            return
        self.helper(s + "0", k, res, n)
        self.helper(s + "1", k, res, n)

    def generateValidStrings(self, n: int, k: int) -> list[str]:
        res = []
        self.helper("", k, res, n)
        return res
