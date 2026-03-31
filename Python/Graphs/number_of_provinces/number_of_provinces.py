# LeetCode 547. Number of Provinces

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        res = 0

        for i in range(n):
            if visited[i]:
                continue
            stack = [i]
            visited[i] = True
            while stack:
                cur = stack.pop()
                for neighbor, v in enumerate(isConnected[cur]):
                    if v == 1 and not visited[neighbor]:
                        stack.append(neighbor)
                        visited[neighbor] = True
            res += 1
        
        return res