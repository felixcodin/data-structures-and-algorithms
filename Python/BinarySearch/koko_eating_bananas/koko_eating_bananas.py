# LeetCode 875. Koko Eating Bananas

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left = 1
        right = max(piles)

        res = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            fits = True
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
                if hours > h:
                    fits = False
                    break
            if fits:
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1
        
        return res
