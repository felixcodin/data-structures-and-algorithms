#Given an integer array nums of unique elements, return all possible subsets (the power set).

class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = []

        for mask in range(1 << n):
            res.append([nums[i] for i in range(n) if (mask & (1 << i))])
        
        return res