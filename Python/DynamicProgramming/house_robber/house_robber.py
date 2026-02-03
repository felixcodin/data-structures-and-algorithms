# LeetCode 198. House Robber

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        p2 = 0
        p1 = 0

        for num in nums:
            cur = max(p1, p2 + num)
            p2 = p1
            p1 = cur

        return p1
