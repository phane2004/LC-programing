class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        vis = [False] * n

        for node, c in edges:
            vis[c] = True
        res = []
        #print(vis)
        for i in range(n):
            #print(not vis[i])
            if not vis[i]:
                res.append(i)
        return res

