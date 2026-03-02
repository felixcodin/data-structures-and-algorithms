# LeetCode 643. Maximum Average Subarray I

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        res = window

        left = 0
        right = k
        while right < len(nums):
            window += nums[right] - nums[left]
            left += 1
            right += 1
            res = max(window, res)
        
        return res/k