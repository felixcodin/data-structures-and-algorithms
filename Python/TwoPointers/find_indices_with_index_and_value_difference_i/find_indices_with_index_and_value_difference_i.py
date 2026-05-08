# LeetCode 2903. Find Indices With Index and Value Difference I

from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mx_idx = 0
        mn_idx = 0
        for j in range(indexDifference, len(nums)):
            i = j - indexDifference
            if nums[mx_idx] < nums[i]:
                mx_idx = i
            if nums[mn_idx] > nums[i]:
                mn_idx = i
            
            if abs(nums[mx_idx] - nums[j]) >= valueDifference:
                return [mx_idx, j]
            if abs(nums[mn_idx] - nums[j]) >= valueDifference:
                return [mn_idx, j]
                
        return [-1, -1]