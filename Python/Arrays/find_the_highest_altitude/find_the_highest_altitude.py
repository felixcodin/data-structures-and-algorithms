# LeetCode 1732. Find the Highest Altitude

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)

        cur = 0
        res = 0
        for num in gain:
            cur += num
            res = max(res, cur)

        return res