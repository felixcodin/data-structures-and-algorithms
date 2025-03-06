#Given an integer array nums of unique elements, return all possible subsets (the power set).

class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = []

        for mask in range(1 << n):
            res.append([nums[i] for i in range(n) if (mask & (1 << i))])
        
        return res

def test_subsets():
    solution = Solution()

    # Test case 1: General case with three elements
    result = solution.subsets([1, 2, 3])
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(result) == sorted(expected)

    # Test case 2: Single element array
    result = solution.subsets([1])
    expected = [[], [1]]
    assert sorted(result) == sorted(expected)

    # Test case 3: Two elements array
    result = solution.subsets([1, 2])
    expected = [[], [1], [2], [1, 2]]
    assert sorted(result) == sorted(expected)

    # Test case 4: Empty array
    result = solution.subsets([])
    expected = [[]]
    assert sorted(result) == sorted(expected)

    # Test case 5: Four elements array
    result = solution.subsets([1, 2, 3, 4])
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
    assert sorted(result) == sorted(expected)

    # Test case 6: Array with negative numbers
    result = solution.subsets([-1, -2, -3])
    expected = [[], [-1], [-2], [-1, -2], [-3], [-1, -3], [-2, -3], [-1, -2, -3]]
    assert sorted(result) == sorted(expected)

    # Test case 7: Array with mixed positive and negative numbers
    result = solution.subsets([-1, 0, 1])
    expected = [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]
    assert sorted(result) == sorted(expected)

    # Test case 8: Array with larger numbers
    result = solution.subsets([10, 20, 30])
    expected = [[], [10], [20], [10, 20], [30], [10, 30], [20, 30], [10, 20, 30]]
    assert sorted(result) == sorted(expected)

    # Test case 9: Array with non-sequential numbers
    result = solution.subsets([5, 10, 15])
    expected = [[], [5], [10], [5, 10], [15], [5, 15], [10, 15], [5, 10, 15]]
    assert sorted(result) == sorted(expected)

    # Test case 10: Array with duplicate elements (though the problem states unique elements, it's good to test)
    result = solution.subsets([1, 1])
    expected = [[], [1], [1], [1, 1]]
    assert sorted(result) == sorted(expected)

# Run the test cases
test_subsets()
print("All test cases passed!")

