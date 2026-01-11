# LeetCode 11. Container With Most Water

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        
        left = 0
        right = len(heights) - 1
        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            area = (right - left) * (left_height if left_height < right_height else right_height)
            max_area = max(max_area, area)
            if left_height <= right_height:
                left += 1
            elif left_height > right_height:
                right -= 1

        return max_area