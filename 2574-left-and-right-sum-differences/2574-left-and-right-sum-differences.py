class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        rightSum = sum(nums)
        leftSum = 0

        for i in range(n):
            rightSum -= nums[i]
            res.append(abs(leftSum - rightSum))
            leftSum += nums[i]
        return res