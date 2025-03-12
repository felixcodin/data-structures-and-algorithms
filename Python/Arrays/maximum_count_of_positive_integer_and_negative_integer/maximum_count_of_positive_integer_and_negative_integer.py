#Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
#In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
#Note that 0 is neither positive nor negative.

class Solution:
    def findFirstPositive(self, nums):
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def maximumCount(self, nums):
        startPositive = self.findFirstPositive(nums)
        countZero = 0

        while startPositive < len(nums) and nums[startPositive] == 0:
            countZero += 1
            startPositive += 1
    
        countPositive = len(nums) - startPositive 
        countNegative = len(nums) - countPositive - countZero


        return max(countNegative, countPositive)