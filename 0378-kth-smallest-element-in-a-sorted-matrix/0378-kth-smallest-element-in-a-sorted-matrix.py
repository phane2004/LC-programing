class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for li in matrix:
            for val in li:
                l.append(val)
        l.sort()
        #print(l)
        return l[k - 1]