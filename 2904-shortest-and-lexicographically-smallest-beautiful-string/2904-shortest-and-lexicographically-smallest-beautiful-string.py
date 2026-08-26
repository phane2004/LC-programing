class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # if all(s[i] == '0' for i in range(len(s)) or s.count('1') != k):
        #     return ""
        if s.count("1") < k:
            return ""
        curr_s = ""
        res = s
        left = 0
        right = 0
        while right <= len(s):
            # print(left, right, res)
            curr_s = s[left:right]
            #print(curr_s)
            if curr_s.count("1") == k:
                if(len(curr_s) < len(res)):
                    res = curr_s
                elif(len(curr_s) == len(res)):
                    res = min(curr_s, res)
                left += 1
                while left < len(s) and s[left] != "1":
                    
                    left += 1
                if left > right:
                    right = left
            elif curr_s.count("1") < k:
                right += 1
            else:
                left += 1
            #print('100011' < '11001')
            #print(res, left, right)
        
        return res
