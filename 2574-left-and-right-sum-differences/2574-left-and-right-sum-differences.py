class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum, rightSum = [], []

        for i in range(n):
            leftSum.append(sum(nums[:i]))
        for j in range(n - 1, -1, -1):
            rightSum.append(sum(nums[j + 1:]))
        # print(leftSum, rightSum)
        res = []

        for i in range(n):
            res.append(abs(leftSum[i] - rightSum[n - i - 1]))
        return res