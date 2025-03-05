#Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
#A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

def longestConsecutive(nums):
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

def test_longestConsecutive():
    # Test case 1: General case with mixed numbers
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    
    # Test case 2: Array with duplicate elements
    assert longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]) == 7
    
    # Test case 3: Array with negative and positive numbers
    assert longestConsecutive([-1, -2, -3, 0, 1, 2, 3]) == 7
    
    # Test case 4: Array with all elements the same
    assert longestConsecutive([1, 1, 1, 1]) == 1
    
    # Test case 5: Array with no consecutive sequence
    assert longestConsecutive([10, 20, 30, 40]) == 1
    
    # Test case 6: Empty array
    assert longestConsecutive([]) == 0
    
    # Test case 7: Array with one element
    assert longestConsecutive([5]) == 1
    
    # Test case 8: Array with two elements
    assert longestConsecutive([1, 2]) == 2
    
    # Test case 9: Array with large range of numbers
    assert longestConsecutive([10, 5, 12, 3, 55, 30, 4, 11, 6, 7, 8, 9]) == 10
    
    # Test case 10: Array with negative numbers only
    assert longestConsecutive([-5, -4, -3, -2, -1]) == 5

# Run the test cases
test_longestConsecutive()
print("All test cases passed!")



