class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {}

        for val in nums:
            if val not in freq:
                freq[val] = 0
            if freq[val] < 2:
                freq[val] += 1
        # print(freq)
        res = []
        for k, v in freq.items():
            res.extend([k] * v)
        # print(res)
        ans = len(res)
        for idx, val in enumerate(res):
            nums[idx] = val
        return ans
