class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(r,c):
            nonlocal res
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            count = 1
            
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            #print(count)
            return count
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
                    #print(res)
                    
        return res