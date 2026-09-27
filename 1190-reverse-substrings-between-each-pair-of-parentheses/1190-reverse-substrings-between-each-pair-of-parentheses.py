from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=deque()
        r=[]
        for i in s:
            if i=="(":
                st.append(len(r))
            elif i==")":
                a=st.pop()
                r[a:]=reversed(r[a:])
            else:
                r.append(i)
        return "".join(r)

        