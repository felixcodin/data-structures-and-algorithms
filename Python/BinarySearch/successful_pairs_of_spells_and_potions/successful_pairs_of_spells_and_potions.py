# LeetCode 2300. Successful Pairs of Spells and Potions

from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        res = []
        n = len(potions)
        for spell in spells:
            left = 0
            right = n - 1
            if (potions[right] * spell < success):
                res.append(0)
                continue
            while left < right:
                mid = left + (right - left) // 2
                product = potions[mid] * spell
                if product >= success:
                    right = mid
                else:
                    left = mid + 1
            res.append(n - left)
        return res