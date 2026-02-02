# LeetCode 695. Max Area of Island

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return 0
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            area = 1
            area += dfs(r, c + 1)
            area += dfs(r + 1, c)
            area += dfs(r, c - 1)
            area += dfs(r - 1, c)

            return area
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    result = max(dfs(i, j), result)

        return result

