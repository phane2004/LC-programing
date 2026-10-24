class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = 1
        lpre = []

        for num in nums:
            lp *= num
            lpre.append(lp)
        rp = 1
        rpre = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            rp *= nums[i]
            rpre[i] = rp
        
        #print(lpre, rpre)
        res = []
        for i in range(len(nums)):
            if (i == 0):
                res.append(rpre[i + 1])
            elif i == len(nums) - 1:
                res.append(lpre[i - 1])
            else:
                res.append(lpre[i - 1] * rpre[i + 1])
        return res
