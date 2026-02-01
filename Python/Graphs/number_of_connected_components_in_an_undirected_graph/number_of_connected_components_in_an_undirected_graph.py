# LeetCode 323. Number of Connected Components in an Undirected Graph

from collections import deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n
        count = 0
        for vertex in range(n):
            if visited[vertex]:
                continue
            q = deque([vertex])
            visited[vertex] = True
            while q:
                curr = q.popleft()
                for v in adj_list[curr]:
                    if not visited[v]:
                        q.append(v)
                        visited[v] = True
            count += 1
        return count