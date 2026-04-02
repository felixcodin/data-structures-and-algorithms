# LeetCode 399. Evaluate Division

from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)

        for i, [u, v] in enumerate(equations):
            adj_list[u].append((v, values[i]))
            adj_list[v].append((u, 1/values[i]))
        
        res = []
        for u, v in queries:
            if u not in adj_list or v not in adj_list:
                res.append(-1)
                continue
            if u == v:
                res.append(1)
                continue
            visited = set()
            found = False
            stack = [(u, 1)]
            visited.add(u)
            while stack:
                cur_node, cur_product = stack.pop()

                if cur_node == v:
                    res.append(cur_product)
                    found = True
                    break

                for neighbor, weight in adj_list[cur_node]:
                    if neighbor not in visited:
                        stack.append((neighbor, cur_product * weight))
                        visited.add(neighbor)
            
            if not found:
                res.append(-1)
        
        return res
