class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        bool = [False for _ in range(len(nums))]

        def helper(temp):
            if len(temp) == len(nums):
                res.append(temp[:])
                return

            for i in range(len(nums)):
                # print(bool)
                if bool[i] == True:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not bool[i - 1]:
                    continue
                temp.append(nums[i])
                bool[i] = True
                helper(temp)
                temp.pop()
                bool[i] = False

        helper([])
        return res
