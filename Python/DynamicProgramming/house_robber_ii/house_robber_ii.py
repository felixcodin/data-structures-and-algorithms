# LeetCode 213. House Robber II

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def dp(i, j):
            p = [0, 0]
            for k in range(i, j):
                cur = max(p[1], p[0] + nums[k])
                p[0] = p[1]
                p[1] = cur 
            return p[1]

        return max(dp(0, n-1), dp(1, n))