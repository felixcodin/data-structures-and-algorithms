# LeetCode 746. Min Cost Climbing Stairs

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p = [0, 0]

        for c in cost:
            mn = min(p)
            p[0] = p[1]
            p[1] = c + mn

        return min(p)