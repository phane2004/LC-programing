class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        res = 0
        preSum = 0
        for val in gain:
            preSum += val
            res = max(res, preSum)
        return res