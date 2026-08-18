class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = defaultdict(list)
        n = len(nums)
        for i in range(0, n):
            if i + k <= n:
                l = nums[i: i + k]
            else:
                break
            for j in range(0, len(l)):
                freq[l[j]].append(i)
    
        ans = -1
        for k, v in freq.items():
            if len(set(v)) == 1:
                ans = max(ans, k)
        return ans