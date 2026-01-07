# LeetCode 463. Island Perimeter

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        
        result = 0
        for i in range(row):
            col = len(grid[i])
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    result += 1
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    result += 1
                if i + 1 >= row or grid[i + 1][j] == 0:
                    result += 1
                if j + 1 >= col or grid[i][j + 1] == 0:
                    result += 1

        return result