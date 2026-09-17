class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = pref.copy()
        for i in range(1, len(pref)):
            res[i] = pref[i - 1] ^ res[i]
        return res