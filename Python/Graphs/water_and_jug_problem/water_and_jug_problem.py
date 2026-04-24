# LeetCode 365. Water and Jug Problem

import math


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        else:
            return target % math.gcd(x, y) == 0