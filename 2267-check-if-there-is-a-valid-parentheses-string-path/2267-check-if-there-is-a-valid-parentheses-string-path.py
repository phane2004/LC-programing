class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        r = 0
        c = 0
        n, m = len(grid), len(grid[0])

        if (grid[0][0] == ')') or (grid[n - 1][m - 1] == '('):
            return False
        @cache
        def helper(r, c, count):
            if r == n - 1 and c == m - 1:
                return count == 1

            if grid[r][c] == '(':
                if r < n - 1 and helper(r + 1, c, count + 1):
                    return True
                if c < m - 1 and helper(r, c + 1, count + 1):
                    return True
            else:
                if count == 0:
                    return False
                if r < n - 1 and helper(r + 1, c, count - 1):
                    return True
                if c < m - 1 and helper(r, c + 1, count - 1):
                    return True
            return False
        return helper(0, 0, 0)
            