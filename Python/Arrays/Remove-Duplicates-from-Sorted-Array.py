class Solution:
    def removeDuplicates(self, nums):
        prev = 0

        for cur in range(1, len(nums)):
            if nums[cur] != nums[prev]:
                prev += 1
                nums[prev] = nums[cur]
        
        return prev + 1
    
def test_removeDuplicates():
    solution = Solution()

    # Test case 1: General case with duplicates
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(nums)
    assert nums[:k] == [0, 1, 2, 3, 4]

    # Test case 2: No duplicates
    nums = [1, 2, 3, 4, 5]
    k = solution.removeDuplicates(nums)
    assert nums[:k] == [1, 2, 3, 4, 5]

    # Test case 3: All elements are the same
    nums = [1, 1, 1, 1, 1]
    k = solution.removeDuplicates(nums)
    assert nums[:k] == [1]

    # Test case 4: Single element array
    nums = [1]
    k = solution.removeDuplicates(nums)
    assert nums[:k] == [1]

    # Test case 5: Two elements, no duplicates
    nums = [1, 2]
    k = solution.removeDuplicates(nums)
    assert nums[:k] == [1, 2]

    # Test case 6: Two elements, with duplicates
    nums = [1, 1]
    k = solution.removeDuplicates(nums)
    assert nums[:k] == [1]

    # Test case 7: Large array with duplicates
    nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    k = solution.removeDuplicates(nums)
    assert nums[:k] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test case 8: Array with negative numbers
    nums = [-3, -3, -2, -2, -1, -1, 0, 0, 1, 1]
    k = solution.removeDuplicates(nums)
    assert nums[:k] == [-3, -2, -1, 0, 1]

    # Test case 9: Array with mixed positive and negative numbers
    nums = [-1, -1, 0, 0, 1, 1, 2, 2]
    k = solution.removeDuplicates(nums)
    assert nums[:k] == [-1, 0, 1, 2]

    # Test case 10: Empty array
    nums = []
    k = solution.removeDuplicates(nums)
    assert nums[:k] == []

test_removeDuplicates()
print("All test cases passed!")