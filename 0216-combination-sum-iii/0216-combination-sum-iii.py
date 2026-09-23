class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        def helper(lth, s,temp, idx):
            if lth == 0 and s == 0:
                res.append(temp[:])
                return

            for i in range(idx, 10):
                if i > s or lth <= 0:
                    break
                temp.append(i)
                helper(lth - 1, s - i,temp, i + 1)
                temp.pop()
        helper(k, n,[], 1)
        return res