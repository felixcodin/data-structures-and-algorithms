# LeetCode 152. Maximum Product Subarray

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            cur_min = min(nums[i], prev_max * nums[i], prev_min * nums[i])
            
            prev_max = cur_max
            prev_min = cur_min
            
            res = max(res, cur_max)
        
        return res