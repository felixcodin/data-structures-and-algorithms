#You are given an integer array `nums` of length n and a 2D array queries where queries[i] = [li, ri, vali].
#Each queries[i] represents the following action on nums:
# - Decrement the value at each index in the range [li, ri] in nums by at most vali.
# - The amount by which each value is decremented can be chosen independently for each index.
#A Zero Array is an array with all its elements equal to 0.
#Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence,
#nums becomes a Zero Array. If no such k exists, return -1.



class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]], k: int) -> bool:
        n = len(nums)
        totalSum = 0
        diff = [0] * (n + 1)

        for i in range(k):
            li, ri, vali = queries[i]
            diff[li] += vali
            diff[ri + 1] -= vali

        for i in range(n):
            totalSum += diff[i]
            if totalSum < nums[i]:
                return False
            
        return True

    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        left = 0
        right = len(queries)

        if not self.isZeroArray(nums, queries, right):
            return -1

        while left <= right:
            mid = left + (right - left) // 2
            if self.isZeroArray(nums, queries, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left