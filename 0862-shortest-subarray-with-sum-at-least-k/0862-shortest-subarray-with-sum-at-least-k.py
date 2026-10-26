class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = float('inf')
        currSum = 0
        preHeap = []

        for i, num in enumerate(nums):
            currSum += num
            if currSum >= k:
                res = min(res, i + 1)
            while preHeap and currSum - preHeap[0][0] >= k:
                res = min(res, i - heappop(preHeap)[1])
            heappush(preHeap, (currSum, i))
        return res if res != float('inf') else -1