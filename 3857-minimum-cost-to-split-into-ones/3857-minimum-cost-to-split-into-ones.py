class Solution:
    def minCost(self, n: int) -> int:
        sum = 0
        for i in range(1, n):
            sum += i
        return sum