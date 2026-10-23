class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        col = [0] * n

        for i in range(n):
            if col[i] != 0: continue
            q = deque()
            q.append(i)
            col[i] = 1

            while q:
                node = q.popleft()

                for nei in graph[node]:
                    if col[nei] == 0:
                        q.append(nei)
                        col[nei] -= col[node]
                    elif col[nei] == col[node]:
                        return False
        return True