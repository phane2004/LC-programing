class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        total = 0
        currSum = 0
        freq = defaultdict(int)
        for num in nums:
            currSum += num
            if currSum == goal:
                total += 1
            if (currSum - goal) in freq:
                total += freq[currSum - goal]
            freq[currSum] += 1
        return total