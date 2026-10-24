class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        presum = 0
        pre = defaultdict(int)
        pre[0] = 1
        for num in nums:
            presum += num
            mod = presum % k

            if mod < 0:
                mod += k
            if mod in pre:
                count += pre[mod]
            pre[mod] += 1
        return count