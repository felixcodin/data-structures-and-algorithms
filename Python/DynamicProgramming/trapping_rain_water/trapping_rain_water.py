# LeetCode 42. Trapping Rain Water

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]

        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])
            rightMax[n-i-1] = max(rightMax[n-i], height[n-i])
        
        trapped = 0
        for i in range(n):
            water_level = min(leftMax[i], rightMax[i]) - height[i]
            if water_level > 0:
                trapped += water_level
        
        return trapped