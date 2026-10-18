class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        n = len(edges)
        indeg = [0] * (n + 1)
        outdeg = [0] * (n + 1)

        for u, v in edges:
            indeg[v - 1] += 1
            outdeg[u - 1] += 1
        for i in range(n + 1):
            if indeg[i] != 0 and outdeg[i] != 0 or (indeg[i] > 1 or outdeg[i] > 1):
                return i + 1