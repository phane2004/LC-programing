class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_num, min_idx = float('inf'), 0
        max_num, max_idx = float('-inf'), 0
        n = len(nums)
        if n == 1:
            return 1
        for idx, val in enumerate(nums):
            if val < min_num:
                min_num, min_idx = val, idx
            if val > max_num:
                max_num, max_idx = val, idx
        
        ans = float('inf')
        if min_idx < max_idx:
            val = min((max_idx - min_idx), (n - max_idx))
            res1 = (min_idx + val) + 1
            ans = min(ans, res1)
            print("res1", res1)

        if min_idx > max_idx:
            val = min((min_idx - max_idx), (n - min_idx))
            res2 = (max_idx + val) + 1
            ans = min(ans, res2)
            print("res2", res2)

        if (n - max_idx) < (n - min_idx):

            res3 = ((n - max_idx) + min((max_idx - min_idx), (min_idx + 1)))
            ans = min(ans, res3)
            print("res3", res3)

        if (n - min_idx) < (n - max_idx):

            res4 = ((n - min_idx) + min((min_idx - max_idx), (max_idx + 1)))
            ans = min(ans, res4)
            print("res4", res4)
        else:
            res5 = min_idx + (n - max_idx) + 1
            ans = min(ans, res5)
            print("res5", res5)
        return ans


            