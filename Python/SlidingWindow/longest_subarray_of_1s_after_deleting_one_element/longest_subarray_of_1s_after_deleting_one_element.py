# LeetCode 1493. Longest Subarray of 1's After Deleting One Element

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        left = 0
        num_of_zero = 0
        for right in range(n):
            if nums[right] == 0:
                num_of_zero += 1
            while num_of_zero > 1:
                if nums[left] == 0:
                    num_of_zero -= 1
                left += 1
            res = max(res, right - left)

        return res