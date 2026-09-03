class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        min_odd = float('inf')
        min_even = float('inf')
        for val in nums1:
            if val % 2 == 1:
                min_odd = min(val, min_odd)
            if val % 2 == 0:
                min_even = min(min_even, val)
        return min_odd == float('inf') or min_even > min_odd