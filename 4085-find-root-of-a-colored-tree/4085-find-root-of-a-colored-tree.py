class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n = len(colors)
        indeg = [0] * n
        outdeg = [0] * n

        col = {'R':'B', 'B':'W', 'W':'R'}

        for u, v in edges:
            if colors[u] == colors[v]:
                return -1
            
            elif col[colors[u]] == colors[v]:
                if indeg[v] == 1 or outdeg[u] == 2:
                    return -1
                indeg[v] += 1
                outdeg[u] += 1
            else:
                if indeg[u] == 1 or outdeg[v] == 2:
                    return -1
                indeg[u] += 1
                outdeg[v] += 1
        root = -1
        for node in range(n):
            if indeg[node] == 0:
                if root != -1:
                    return -1
                root = node
        return root
