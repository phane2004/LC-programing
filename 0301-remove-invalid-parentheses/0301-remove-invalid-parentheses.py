class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = set()
        @cache
        def helper(o, c, idx, path):
            if idx == len(s):
                if o == c:
                    res.add(path)
                return
            else:
                ch = s[idx]
                if ch != '(' and ch != ')':
                    helper(o, c, idx + 1, path + ch)
                else:
                    helper(o, c, idx + 1, path)
                    if ch == '(':
                        helper(o + 1, c, idx + 1, path + ch)
                    elif c < o:
                        helper(o, c + 1, idx + 1, path + ch)
            
        helper(0, 0, 0, "")
        res = list(res)
        res = sorted(res, key = lambda x : len(x), reverse=True)
        max_len = len(res[0])
        idx = 0
        for ch in res:
            if len(ch) < max_len:
                break
            idx += 1
        #print(res)
        return res[:idx]