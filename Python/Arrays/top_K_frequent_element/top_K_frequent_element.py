#Given an integer array nums and an integer k, return the k most frequent elements within the array.
#Time Complexity: O(n) || Space Complexity: O(n)

class Solution:
    def topKFrequent(self, nums, k):
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