# LeetCode 485. Max Consecutive Ones

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0

        return res if res > count else count