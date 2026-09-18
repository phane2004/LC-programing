class Solution:
    def helper(self, s, n, uniq):
        
        if n == 0:
            if len(s) < 2:
                uniq.add(s)
                
            elif len(s) >= 2:
                if any((s[i] == '0' and s[i - 1] == '0' for i in range(1, len(s)))):
                    return
                else:
                    uniq.add(s)
            #print(uniq)
            return

        self.helper(s + '0', n - 1, uniq)
        self.helper(s + '1', n - 1, uniq)
    def validStrings(self, n: int) -> List[str]:
        uniq = set()
        self.helper("", n, uniq)
        return list(uniq)
        