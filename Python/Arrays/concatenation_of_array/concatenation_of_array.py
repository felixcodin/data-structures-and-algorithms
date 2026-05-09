# LeetCode 1929. Concatenation of Array

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            nums.append(nums[i])
        
        return nums