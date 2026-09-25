class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def helper(temp):
            if temp and len(nums) == len(temp):
                res.append(temp[:])
                return

            for idx, val in enumerate(nums):
                if val in temp:
                    continue
                temp.append(val)
                helper(temp)
                temp.pop()
        helper([])
        return res