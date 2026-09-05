class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_val = float('-inf')
        min_val = [0] * n
        val = float('inf')
        for i in range(n - 1, -1, -1):
            val = min(val, nums[i])
            min_val[i] = val
        for i in range(n):
            max_val = max(nums[i], max_val)
            if max_val - min_val[i] <= k:
                return i
        return -1