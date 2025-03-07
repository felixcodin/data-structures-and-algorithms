class Solution:
    def removeDuplicates(self, nums):
        prev = 0

        for cur in range(1, len(nums)):
            if nums[cur] != nums[prev]:
                prev += 1
                nums[prev] = nums[cur]
        
        return prev + 1