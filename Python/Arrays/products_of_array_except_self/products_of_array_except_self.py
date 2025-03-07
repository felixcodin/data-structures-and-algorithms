#Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
#Time Complexity: O(n) || Space Complexity: O(n)

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res