class Solution:
    def minInsertions(self, s: str) -> int:
        idx = 0
        open = 0
        insert = 0

        while idx < len(s):
            if s[idx] == '(':
                open += 1
                idx += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    insert += 1
                if idx < len(s) - 1 and s[idx + 1] == ')':
                    idx += 2
                else:
                    insert += 1
                    idx += 1
        # print(open, insert)
        return insert + open * 2