class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i in range(n):
            res.append(abs(sum(nums[:i]) - sum(nums[i + 1:])))
        return res