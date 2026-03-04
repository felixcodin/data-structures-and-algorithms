# LeetCode 1004. Max Consecutive Ones III

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
            res = 0
            left = 0
            right = 0

            n = len(nums)
            cnt = 0
            while right < n:
                if nums[right] == 0:
                    cnt += 1
                right += 1
                
                while k - cnt < 0:
                    if nums[left] == 0:
                        cnt -= 1
                    left += 1

                res = max(res, right - left)

            return res