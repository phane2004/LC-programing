class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        meet = [0] * n

        for node,ch in trust:
            meet[ch - 1] += 1
            meet[node - 1] -= 1
        ans = -1
        #print(meet)
        for i in range(n):
            if meet[i] == n - 1:
                ans = i + 1
        return ans