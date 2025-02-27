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

def test_maximumSubarray():
    solution = Solution()

    # Test case 1: General case with mixed positive and negative numbers
    assert solution.maximumSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    # Test case 2: All positive numbers
    assert solution.maximumSubarray([1, 2, 3, 4, 5]) == 15

    # Test case 3: All negative numbers
    assert solution.maximumSubarray([-1, -2, -3, -4, -5]) == -1

    # Test case 4: Single element array
    assert solution.maximumSubarray([5]) == 5

    # Test case 5: Single negative element array
    assert solution.maximumSubarray([-5]) == -5

    # Test case 6: Array with zeros
    assert solution.maximumSubarray([0, -3, 1, 1, -1, 0, 2, -2]) == 3

    # Test case 7: Large array with mixed numbers
    assert solution.maximumSubarray([10, -3, 4, -1, 2, 1, -5, 4, 6, -2, 3, -1, 2, -4, 5]) == 21

    # Test case 8: Array with increasing sequence
    assert solution.maximumSubarray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55

    # Test case 9: Array with decreasing sequence
    assert solution.maximumSubarray([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 55

    # Test case 10: Array with alternating positive and negative numbers
    assert solution.maximumSubarray([1, -1, 2, -2, 3, -3, 4, -4, 5, -5]) == 5

test_maximumSubarray()
print("All test cases passed!")