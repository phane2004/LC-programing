class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = []

        def helper(sub, idx):
            if len(sub) == len(s):
                res.append(sub)
            
            else:
                if s[idx].isalpha():
                    helper(sub + s[idx].swapcase(), idx + 1)
                helper(sub + s[idx], idx + 1)
        helper("", 0)
        return res

            
        