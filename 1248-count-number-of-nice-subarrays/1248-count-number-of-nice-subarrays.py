class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        total = 0
        currSum = 0
        pre = defaultdict(int)
        pre[0] = 1

        for i in range(len(nums)):
            currSum += nums[i] % 2

            if (currSum - k) in pre:
                total += pre[currSum - k]
                #print(total, pre)
            pre[currSum] += 1
        return total