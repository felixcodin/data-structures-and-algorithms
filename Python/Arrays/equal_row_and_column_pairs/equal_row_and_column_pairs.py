# LeetCode 2352. Equal Row and Column Pairs

from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows_map = defaultdict(int)
        res = 0

        n = len(grid)
        for i in range(n):
            rows_map[tuple(grid[i])] += 1

        for i in range(n):
            column = tuple([row[i] for row in grid])
            if column in rows_map:
                res += rows_map[column]

        return res