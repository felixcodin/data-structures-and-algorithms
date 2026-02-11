# LeetCode 300. Longest Increasing Subsequence

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for i in range(len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                continue

            left = 0
            right = len(dp)
            while left <= right:
                mid = left + (right - left) // 2
                if dp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            dp[left] = nums[i]
        
        return len(dp)