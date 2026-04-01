# LeetCode 1466. Reorder Routes to Make All Paths Lead to the City 

from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        original_path = set()

        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)

            original_path.add((u, v))
        
        res = 0
        visited = [False] * n
        stack = [0]
        visited[0] = True
        while stack:
            cur = stack.pop()
            for nei in adj_list[cur]:
                if not visited[nei]:
                    stack.append(nei)
                    visited[nei] = True

                    if (cur, nei) in original_path:
                        res += 1
        
        return res