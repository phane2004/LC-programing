class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        premap = defaultdict(int)

        premap[0] = 1
        s, count = 0, 0
        for num in nums:
            s += num
            if (s - k) in premap:
                count += premap[s - k]
            premap[s] += 1
        return count