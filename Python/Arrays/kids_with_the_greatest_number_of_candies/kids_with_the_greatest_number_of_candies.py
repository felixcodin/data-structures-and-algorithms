# LeetCode 1431. Kids With the Greatest Number of Candies

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [False] * n

        max_candies = max(candies)
        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                result[i] = True
        
        return result