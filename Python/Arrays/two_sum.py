#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

class Solutions_twoSum:
    def twoSum(self, nums, target):
        indices = {}

        for index, number in enumerate(nums):
            indices[number] = index
        
        for index, number in enumerate(nums):
            diff = target - number
            if diff in indices and indices[diff] != index:
                return [index, indices[diff]]

test_case = Solutions_twoSum()
print(test_case.twoSum(nums = [1, 3, 5, 7, 9, 4], target = 7))