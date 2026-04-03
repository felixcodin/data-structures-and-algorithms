# LeetCode 1926. Nearest Exit from Entrance in Maze

from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start_r, start_c = entrance

        queue = deque([(start_r, start_c, 0)])
        
        maze[start_r][start_c] = '+'

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c, steps = queue.popleft()

            if (r != start_r or c != start_c) and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    queue.append((nr, nc, steps + 1))

                    maze[nr][nc] = '+'
        
        return -1