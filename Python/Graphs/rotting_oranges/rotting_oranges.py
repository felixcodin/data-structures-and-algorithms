# LeetCode 994. Rotting Oranges

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        
        minutes = 0
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        directions = [(0, -1), (1, 0), (0,  1), (-1, 0)]
        while queue:
            q_size = len(queue)
            for _ in range(q_size):
                cur_r, cur_c = queue.popleft()
                for dr, dc in directions:
                    nr = cur_r + dr
                    nc = cur_c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
                        if fresh == 0:
                            return minutes + 1
            minutes += 1
        
        return -1