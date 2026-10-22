class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = set()
        m, n = len(grid), len(grid[0])
        count = 0
        def dfs(r, c):
            if 0 > r or r >= m or 0 > c or c >= n or grid[r][c] == '0' or (r, c)  in vis:
                return
            vis.add((r, c))
            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r,c) not in vis:
                    count += 1
                    #print(vis)
                    dfs(r, c)
        return count
