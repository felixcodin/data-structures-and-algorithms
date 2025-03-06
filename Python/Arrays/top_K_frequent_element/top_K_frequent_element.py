#Given an integer array nums and an integer k, return the k most frequent elements within the array.
#Time Complexity: O(n) || Space Complexity: O(n)

def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)] #it is used to store numbers whose frequency matches the index of the list.

    for n in nums:
        count[n] = 1 + count.get(n, 0) #A hash map where the key is a number from the list and the value is the frequency of that number.
    for n, c in count.items():
        freq[c].append(n) #Add the number to the 'freq' list at the index corresponding to its frequency.

    res = []
    for i in range(len(nums) - 1, 0, -1):
        for num in freq[i]:
            res.append(num) #Add to the 'res' list the numbers with frequencies from highest to lowest until the number of elements equals 'k'.
            if len(res) == k:
                return res


# Test cases
test_cases = [
    ([1, 1, 1, 2, 2, 3], 2),  # Easy case
    ([1], 1),  # Single element
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),  # All unique elements
    ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 5),  # Multiple elements with same frequency
    ([4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 1),  # All elements are the same
    ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2),  # Elements with increasing frequency
    ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10], 10),  # Large k value
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),  # Elements with equal frequency
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),  # Larger array with repeated elements
    ([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10], 10)  # Worst case with maximum frequency elements
]

for i, (nums, k) in enumerate(test_cases):
    print(f"Test case {i+1}: nums = {nums}, k = {k}")
    print(f"Output: {topKFrequent(nums, k)}\n")