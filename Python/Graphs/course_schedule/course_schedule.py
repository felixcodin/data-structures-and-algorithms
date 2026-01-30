# LeetCode 207. Course Schedule

from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[v].append(u)
        
        visited = set()
        path = set()
        def dfs(v):
            if v in visited:
                return True
            if v in path:
                return False

            path.add(v)
            for u in adj_list[v]:
                if u in path:
                    return False
                if u not in visited:
                    if not dfs(u):
                        return False
            
            path.remove(v)
            visited.add(v)
            return True

        for vertex in range(numCourses):
            if not dfs(vertex):
                return False
        return True