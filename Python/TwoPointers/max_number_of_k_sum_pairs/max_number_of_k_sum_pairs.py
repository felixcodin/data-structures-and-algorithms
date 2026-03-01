# LeetCode 1679. Max Number of K-Sum Pairs

from collections import defaultdict
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0

        # Time Complexity: O(nlogn)
        # Space Complexity: O(1)
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if k - nums[left] == nums[right]:
                res += 1
                left += 1
                right -= 1
            elif k - nums[left] > nums[right]:
                left += 1 
            else:
                right -= 1

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        """
        mp = defaultdict(int)
        
        for num in nums:
            if mp[num] > 0:
                res += 1
                mp[num] -= 1
            else:
                mp[k - num] += 1
        """
        return res