# LeetCode 417. Pacific Atlantic Water Flow

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        visited_pacific = [[False for i in range(m)] for j in range(n)]
        visited_atlantic = [[False for i in range(m)] for j in range(n)]

        def dfs(r, c, visited):
            visited[r][c] = True

            if r > 0 and visited[r-1][c] == False and heights[r-1][c] >= heights[r][c]:
                dfs(r-1, c, visited)
            if r < n - 1 and visited[r+1][c] == False and heights[r+1][c] >= heights[r][c]:
                dfs(r+1, c, visited)
            if c > 0 and visited[r][c-1] == False and heights[r][c-1] >= heights[r][c]:
                dfs(r, c-1, visited)
            if c < m - 1 and visited[r][c+1] == False and heights[r][c+1] >= heights[r][c]:
                dfs(r, c+1, visited)
            
        for i in range(n):
            dfs(i, 0, visited_pacific)
            dfs(i, m-1, visited_atlantic)
        for i in range(m):
            dfs(0, i, visited_pacific)
            dfs(n-1, i, visited_atlantic)

        res = []
        for i in range(n):
            for j in range(m):
                if visited_pacific[i][j] and visited_atlantic[i][j]:
                    res.append([i, j])

        return res
