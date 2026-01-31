# LeetCode 261. Graph Valid Tree

from collections import defaultdict, deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return False
        if n - 1 != len(edges):
            return False

        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = {0}
        q = deque([0])
        while q:
            curr = q.popleft()
            for v in adj_list[curr]:
                if v not in visited:
                    q.append(v)
                    visited.add(v)

        return len(visited) == n