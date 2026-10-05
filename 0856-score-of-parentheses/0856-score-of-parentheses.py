class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]

        for idx, ch in enumerate(s): #(()) 0 -- 0 -- 1|| 
            if ch == '(':
                if s[idx + 1] == ')':
                    stk.append(1)
                else:
                    stk.append(0)
            else:
                score = stk.pop()
                stk[-1] += 2 * score
        return stk[0] // 2
                