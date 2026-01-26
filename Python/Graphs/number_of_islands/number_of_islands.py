# LeetCode 200. Number of Islands

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return False

            if grid[i][j] == "0":
                return False

            grid[i][j] = "0"
            for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + d1, j + d2);
            
            return True

        count = 0
        for i in range(n):
            for j in range(m):
                if dfs(i, j):
                    count += 1
        return count          