# LeetCode 79. Word Search

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        
        n = len(board)
        m = len(board[0])

        def dfs(char_index, i, j):
            if i < 0 or i >= n or j < 0 or j >= m or word[char_index] != board[i][j]:
                return False
            
            if char_index == len(word) - 1:
                return True

            temp = board[i][j]
            board[i][j] = '#'

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni = i + di
                nj = j + dj
                if dfs(char_index + 1, ni, nj):
                    board[i][j] = temp
                    return True

            board[i][j] = temp
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(0, i, j):
                    return True
        return False