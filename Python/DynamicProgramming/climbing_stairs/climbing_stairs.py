# LeetCode 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        p1 = 1
        p2 = 2

        for _ in range(3, n + 1):
            curr = p1 + p2
            p1 = p2
            p2 = curr

        return p2