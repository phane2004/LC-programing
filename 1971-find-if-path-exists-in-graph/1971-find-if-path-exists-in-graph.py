class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        print(edges)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        q = [source]
        visited = {source}
        while q:
            node = q.pop(0)
            for j in graph[node]:
                if j == destination:
                    return True
                if j not in visited:
                    q.append(j)
                    visited.add(j)
        return False