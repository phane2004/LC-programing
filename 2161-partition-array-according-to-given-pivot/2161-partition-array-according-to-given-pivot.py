class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        eq = []
        more = []
        for val in nums:
            if val < pivot:
                less.append(val)
            elif val == pivot:
                eq.append(val)
            else:
                more.append(val)
        return less + eq + more