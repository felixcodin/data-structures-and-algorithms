#Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maximumSubarray(self, nums):
        if len(nums) == 1:
            return nums[0]

        res = nums[0]
        cur = 0

        for n in nums:
            cur += n

            res = cur if cur > res else res

            if cur < 0:
                cur = 0
            
        return res