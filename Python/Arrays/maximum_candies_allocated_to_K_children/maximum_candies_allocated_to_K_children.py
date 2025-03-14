#You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i].
#You can divide each pile into any number of sub piles, but you cannot merge two piles together.
#You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies.
#Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.

#Return the maximum number of candies each child can get.

class Solution:
    def canDivideCandies(self, candies: list[int], k: int, c: int) -> bool:
        total = 0
        for item in candies:
            total += (item // c)

        if total < k:
            return False

        return True

    def maximumCandies(self, candies: list[int], k: int) -> int:
        left = 1
        right = max(candies)

        while left <= right:
            mid = (left + right) // 2
            if self.canDivideCandies(candies, k, mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right