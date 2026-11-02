class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        val = nums[n // 2]
        total = 0
        for num in nums:
            total += abs(num - val)
        return total