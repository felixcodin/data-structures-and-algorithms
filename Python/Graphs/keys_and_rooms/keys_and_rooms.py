# LeetCode 841. Keys and Rooms


from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        stack = [0]
        while stack:
            cur = stack.pop()
            visited[cur] = True
            for vertex in rooms[cur]:
                if visited[vertex] == False:
                    stack.append(vertex)
        
        return sum(visited) == n