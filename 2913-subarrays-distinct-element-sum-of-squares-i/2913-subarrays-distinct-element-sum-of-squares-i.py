class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        t=0
        for i in range(len(nums)):
            d=set()
            for j in range(i,len(nums)):
                d.add(nums[j])
                t+=len(d)**2
        return t
        