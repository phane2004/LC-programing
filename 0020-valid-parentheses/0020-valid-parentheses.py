class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in range(len(s)):
            if (s[i] == ')' or s[i] == ']' or s[i] == '}') and len(l) == 0:
                return False
            elif s[i] == '(' or s[i] == '{' or s[i] == '[':
                l.append(s[i])
            else:
                if (s[i] == ')' and l[-1] == '(') or (s[i] == '}' and l[-1] == '{') or (s[i] == ']' and l[-1] == '['):
                    l.pop()
                else:
                    break
        return len(l) == 0
        