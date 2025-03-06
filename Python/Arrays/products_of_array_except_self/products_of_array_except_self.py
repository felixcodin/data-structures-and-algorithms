#Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
#Time Complexity: O(n) || Space Complexity: O(n)

def productExceptSelf(nums):
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

def test_productExceptSelf():
    # Test case 1: General case with positive numbers
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    
    # Test case 2: Array with a zero
    assert productExceptSelf([1, 2, 0, 4]) == [0, 0, 8, 0]
    
    # Test case 3: Array with multiple zeros
    assert productExceptSelf([0, 0, 0, 0]) == [0, 0, 0, 0]
    
    # Test case 4: Array with negative numbers
    assert productExceptSelf([-1, -2, -3, -4]) == [-24, -12, -8, -6]
    
    # Test case 5: Array with both positive and negative numbers
    assert productExceptSelf([-1, 2, -3, 4]) == [-24, 12, -8, 6]
    
    # Test case 6: Single element array
    assert productExceptSelf([5]) == [1]
    
    # Test case 7: Two elements array
    assert productExceptSelf([3, 4]) == [4, 3]
    
    # Test case 8: Array with all ones
    assert productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]
    
    # Test case 9: Array with large numbers
    assert productExceptSelf([1000, 2000, 3000, 4000]) == [24000000000, 12000000000, 8000000000, 6000000000]
    
    # Test case 10: Array with mixed positive, negative, and zero
    assert productExceptSelf([1, -1, 0, 3, -3]) == [0, 0, 9, 0, 0]

# Run the test cases
test_productExceptSelf()
print("All test cases passed!")