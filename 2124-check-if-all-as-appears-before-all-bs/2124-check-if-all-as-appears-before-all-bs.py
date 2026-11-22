class Solution:
    def checkString(self, s: str) -> bool:
        b = 0
        for ch in s:
            if ch == 'a' and b:
                return False
            if ch == 'b':
                b = 1
        return True