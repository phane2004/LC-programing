class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            ri = dfs(r, c + 1)
            l = dfs(r, c - 1)
            d = dfs(r + 1, c)
            u = dfs(r - 1, c)
            return u and l and ri and d 
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and dfs(r, c):
                    count += 1
        return count
        