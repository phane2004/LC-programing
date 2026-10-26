class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        count = 0
        arr = []
        freq = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count -= 1
            arr.append(count)
            if count not in freq:
                freq[count] = i
            else:
                res = max(res, i - freq[count])
        for j in range(len(arr) - 1, -1, -1):
            if arr[j] == 0:
                res = max(res, j + 1)
        return res