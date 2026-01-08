# LeetCode 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        mx = 1
        mn = 1
        res = 1
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                mx += 1
                mn = 1
            elif nums[i] == nums[i + 1]:
                mx = 1
                mn = 1
            else:
                mn += 1
                mx = 1
            res = max(mn, res, mx)

        return res