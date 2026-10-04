class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        @cache
        def helper(o, c, idx):
            if idx == n:
                return o == c

            if s[idx] == '(':
                return helper(o + 1, c, idx + 1)

            elif s[idx] == ')':
                if c >= o:
                    return False
                return helper(o, c + 1, idx + 1)

            else:  # '*'
                # Treat '*' as '('
                if helper(o + 1, c, idx + 1):
                    return True

                # Treat '*' as ')'
                if c < o and helper(o, c + 1, idx + 1):
                    return True

                # Treat '*' as empty
                if helper(o, c, idx + 1):
                    return True

                return False

        return helper(0, 0, 0)