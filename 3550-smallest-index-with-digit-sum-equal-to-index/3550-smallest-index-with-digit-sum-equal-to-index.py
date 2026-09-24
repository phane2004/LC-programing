class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def total(num):
            sum = 0
            while num > 0:
                rem = num % 10
                sum += rem
                num = num // 10
            return sum

        for idx in range(len(nums)):
            if total(nums[idx]) == idx:
                return idx
        return -1