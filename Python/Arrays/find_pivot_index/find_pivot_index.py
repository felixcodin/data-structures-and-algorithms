# LeetCode 724. Find Pivot Index

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        right_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return i
            left_sum += num
        
        return -1