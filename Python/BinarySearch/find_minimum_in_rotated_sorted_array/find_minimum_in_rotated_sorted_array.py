# LeetCode 153. Find Minimum in Rotated Sorted Array

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mn = nums[left]
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
            mn = min(nums[mid], mn)
        return mn