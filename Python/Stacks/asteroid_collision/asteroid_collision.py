# LeetCode 735. Asteroid Collision

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for aster in asteroids:
            is_alive = True
            while stack and aster < 0 and stack[-1] > 0:
                if abs(aster) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(aster) == stack[-1]:
                    stack.pop()
                is_alive = False
                break

            if is_alive:
                stack.append(aster)
        
        return stack