class Solution:

    def helper(self, g, temp, res, idx):
        temp.append(idx)
        if idx == len(g) - 1:
            res.append(temp.copy())
            temp.pop()
            return
        for node in g[idx]:
            self.helper(g, temp, res, node)
        temp.pop()
            
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        temp = []
        res = []
        self.helper(graph, temp, res, 0)
        return res