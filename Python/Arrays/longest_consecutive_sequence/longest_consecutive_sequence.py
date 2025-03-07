#Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
#A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if n - 1 not in numSet:
                lenght = 0
                while n in numSet:
                    lenght += 1
                    n += 1
                longest = max(longest, lenght)
                
        return longest